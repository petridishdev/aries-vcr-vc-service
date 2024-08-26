import json
from fastapi import APIRouter, Response, status

from schemas import SecuredDocument, SignedCredentialType
from schemas.mappings import VCRCredentialType
from services import vcr as vcr_service

router = APIRouter(prefix="/credential-types", tags=["credential-types"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=SecuredDocument[SignedCredentialType],
    response_model_exclude_none=True,
    response_model_by_alias=True,
)
async def register_credential_type(
    secured_credential_type: SecuredDocument[SignedCredentialType],
):
    """Register a new credential type"""

    try:
        secured_credential_type_data = secured_credential_type.model_dump(
            by_alias=True, exclude_none=True
        )
        vcr_credential_type = VCRCredentialType(**secured_credential_type_data)

        # TODO: This needs to have a defined schema
        data = {
            "issuer": {
                "name": "test-issuer",
                "did": secured_credential_type.secured_document.verification_methods[0],
                "abbreviation": "",
                "email": "",
                "url": "",
            },
            "credential_type": vcr_credential_type.model_dump(
                by_alias=True, exclude_none=True
            ),
        }
        svc_response = await vcr_service.register_credential_type(data)
        # TODO: Log the response
        print(svc_response)
    except Exception as e:
        # TODO: Log the error
        print(e)
        return Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=json.dumps(
                {"error": "There was an error registering the credential type"}
            ),
            media_type="application/json",
        )

    return secured_credential_type
