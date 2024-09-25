from config import settings
from httpx import AsyncClient
from fastapi import HTTPException
from aries_askar.bindings import LocalKeyHandle
from aries_askar import Key
from multiformats import multibase
from hashlib import sha256
import canonicaljson


class AskarVerifier:
    def __init__(self):
        self.type = "DataIntegrityProof"
        self.cryptosuite = "eddsa-jcs-2022"
        self.purpose = "authentication"
        self.issuers = [issuer["id"] for issuer in settings.issuers]

    async def verify_secured_document(self, document: dict):
        proof = document.pop("proof")[0]
        await self._assert_proof(proof)
        await self._verify_proof(document, proof)

    async def resolve_issuer(self, did: str):
        issuer = next(
            (issuer for issuer in settings.issuers if issuer["id"] == did), None
        )
        if not issuer:
            raise HTTPException(status_code=400, detail="Unknown issuer")
        return issuer

    async def _assert_proof(self, proof):
        try:
            assert proof["type"] == self.type, "Invalid proof type"
            assert proof["cryptosuite"] == self.cryptosuite, "Invalid cryptosuite"
            assert proof["proofPurpose"] == self.purpose, "Invalid proof purpose"
            assert (
                proof["verificationMethod"].split("#")[0] in self.issuers
            ), "Unknown issuer"
        except AssertionError as msg:
            raise HTTPException(status_code=400, detail=str(msg))

    async def _verify_proof(self, document, proof):
        try:
            await self._resolve_verification_method(proof["verificationMethod"])
            signature = multibase.decode(proof.pop("proofValue"))
            hash_data = (
                sha256(canonicaljson.encode_canonical_json(document)).digest()
                + sha256(canonicaljson.encode_canonical_json(proof)).digest()
            )
            verified = self.key.verify_signature(message=hash_data, signature=signature)
            if not verified:
                raise HTTPException(
                    status_code=400, detail="Signature was forged or corrupt."
                )
        except:
            raise HTTPException(status_code=400, detail="Error verifying proof.")

    async def _resolve_verification_method(self, kid):
        did = kid.split("#")[0]
        async with AsyncClient() as client:
            r = await client.get(f"https://{did[8:].replace(':', '/')}/did.json")
        try:
            did_doc = r.json()
            multikey = next(
                (
                    verification_method["publicKeyMultibase"]
                    for verification_method in did_doc["verificationMethod"]
                    if verification_method["id"] == kid
                ),
                None,
            )
            self.key = Key(LocalKeyHandle()).from_public_bytes(
                alg="ed25519", public=bytes(bytearray(multibase.decode(multikey))[2:])
            )
        except:
            raise HTTPException(
                status_code=400, detail=f"Unable to resolve verification method: {kid}"
            )
