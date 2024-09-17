import json
from fastapi import APIRouter, Response, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.web_requests import (
    RegisterCredentialTypeRequest,
    RegisterCredentialTypeResponse,
)
from app.models.mappings import VCRCredentialType
from app.services import vcr as vcr_service
from app.services import Verifier
from config import settings

router = APIRouter(
    tags=["credential-types"],
    redirect_slashes=False,
)

response_model = {"response_model": RegisterCredentialTypeResponse}


@router.post("/credential-types", status_code=201, **response_model)
async def register_credential_type(
    request_body: RegisterCredentialTypeRequest,
):
    """Register a new credential type"""
    try:
        # Extract credential type and options from request body
        credential_type = request_body.model_dump()["credentialType"]
        options = request_body.model_dump()["options"]

        # Pre verification checks

        # Verify the proof to authenticate the caller
        Verifier().verify_auth_proof(credential_type.copy())

        # Post verification checks
        assert (
            credential_type["proof"][0]["verificationMethod"]
            in credential_type["verificationMethods"]
        ), "verificationMethod mismatch"

        # Derive did from the proof
        did = Verifier().derive_issuer(credential_type["proof"][0])

        # Derive a VCR object from payload mappings
        # TODO: This needs to have a defined schema
        data = {
            "issuer": next(
                (issuer for issuer in settings.ISSUERS if issuer["id"] == did), None
            ),
            "credential_type": VCRCredentialType(
                credential_type=credential_type, options=options
            ).model_dump(),
        }
        await vcr_service.register_credential_type(data)
        return JSONResponse(status_code=201, content=data)
    except Exception as e:
        # TODO: Log the error
        print(e)
        raise HTTPException(
            status_code=500, detail="There was an error registering the credential type."
        )
