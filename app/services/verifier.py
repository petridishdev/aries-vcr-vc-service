from aries_askar import Key
from aries_askar.bindings import LocalKeyHandle
from multiformats import multibase
from fastapi import HTTPException
from hashlib import sha256
from config import settings
import canonicaljson
import requests


class AskarVerifier:
    def __init__(self):
        self.type = "DataIntegrityProof"
        self.cryptosuite = "eddsa-jcs-2022"
        self.issuers = [issuer["id"] for issuer in settings.ISSUERS]

    def _resolve_verification_method(self, kid):
        did = kid.split("#")[0]
        r = requests.get(f"https://{did[8:].replace(':', '/')}/did.json")
        try:
            verification_methods = r.json()["verificationMethod"]
            multikey = next(
                (
                    verification_method["publicKeyMultibase"]
                    for verification_method in verification_methods
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

    def _assert_proof(self, proof, purpose):
        try:
            assert proof["type"] == self.type, "Invalid proof type"
            assert proof["cryptosuite"] == self.cryptosuite, "Invalid cryptosuite"
            assert proof["proofPurpose"] == purpose, "Invalid proof purpose"
            assert (
                proof["verificationMethod"].split("#")[0] in self.issuers
            ), "Unknown issuer"
        except AssertionError as msg:
            raise HTTPException(status_code=400, detail=str(msg))

    def _verify_proof(self, document, proof):
        try:
            self._resolve_verification_method(proof["verificationMethod"])
            signature = multibase.decode(proof.pop("proofValue"))
            hash_data = (
                sha256(canonicaljson.encode_canonical_json(document)).digest()
                + sha256(canonicaljson.encode_canonical_json(proof)).digest()
            )
            if not self.key.verify_signature(message=hash_data, signature=signature):
                raise HTTPException(
                    status_code=400, detail="Signature was forged or corrupt."
                )
        except:
            raise HTTPException(status_code=400, detail="Error verifying proof.")

    def verify_assertion_proof(self, document):
        proof = document.pop("proof")[0]
        self._assert_proof(proof, "assertionMethod")
        # self._verify_proof(document, proof)

    def verify_auth_proof(self, document):
        proof = document.pop("proof")[0]
        self._assert_proof(proof, "authentication")
        # self._verify_proof(document, proof)

    def derive_issuer(self, proof):
        return proof["verificationMethod"].split("#")[0]
