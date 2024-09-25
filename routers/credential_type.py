import json
from fastapi import APIRouter, Response, status

from schemas import SecuredDocument, SignedCredentialType
from schemas.mappings import VCRCredentialType
from services import vcr as vcr_service
from services import Verifier

router = APIRouter(
    prefix="/credential-types",
    tags=["credential-types"],
    redirect_slashes=False,
)

response_model = {
    "response_model": SecuredDocument[SignedCredentialType],
    "response_model_exclude_none": True,
    "response_model_by_alias": True,
}


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    include_in_schema=False,
    **response_model,
)
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    **response_model,
)
async def register_credential_type(
    secured_credential_type: SecuredDocument[SignedCredentialType],
):
    """Register a new credential type"""

    try:
        verifier = Verifier()
        await verifier.verify_secured_document(secured_credential_type.raw_data)
        issuer = await verifier.resolve_issuer(
            secured_credential_type.secured_document.origin_did
        )

        secured_credential_type_data = secured_credential_type.model_dump(
            by_alias=True, exclude_none=True
        )
        vcr_credential_type = VCRCredentialType(**secured_credential_type_data)

        data = {
            "issuer": {
                "name": issuer.get("name"),
                "did": issuer.get("id"),
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
