import json
from fastapi import APIRouter, Response, status, HTTPException
from fastapi.responses import JSONResponse
from config import settings

from app.schemas.web_requests import StoreCredentialRequest, StoreCredentialResponse
from app.schemas.mappings.vcr_credential import VCRCredential
from app.services import vcr as vcr_service
from app.services import Verifier

router = APIRouter(tags=["credentials"], redirect_slashes=False)


response_model = {
    "response_model": StoreCredentialResponse,
    "response_model_exclude_none": True,
    "response_model_by_alias": True,
}


@router.post(
    "/credentials",
    status_code=201,
    **response_model,
)
async def store_credential(request_body: StoreCredentialRequest):
    """Store a new credential"""

    try:
        # Extract VP and options from request body
        vp = request_body.model_dump()["verifiablePresentation"]
        options = request_body.model_dump()["options"]

        # # Pre verification checks
        # assert options["issuerId"] in settings.ISSUERS, "Unknown issuer"

        # Verify VP proof to authenticate the caller
        Verifier().verify_auth_proof(vp.copy())

        # Extract VC from the verified presentation
        vc = vp["verifiableCredential"][0]

        # Verify the assertion proof
        Verifier().verify_assertion_proof(vc.copy())

        # Post verification checks
        assert options["credentialId"] == vc["id"], "Credential ID mismatch"
        assert options["issuerId"] == vc["issuer"]["id"], "Issuer mismatch"
        assert options["credentialType"] in vc["type"], "Credential type mismatch"

        # Derive a VCR object from payload mappings
        vcr_mapped = VCRCredential(credential=vc, options=options).model_dump()

        # Store the credential
        # await vcr_service.store_credential(vcr_mapped)

        return JSONResponse(status_code=201, content=vcr_mapped)
    except Exception as e:
        # TODO: Log the error
        print(e)
        raise HTTPException(
            status_code=500, detail="There was an error storing the credential"
        )
