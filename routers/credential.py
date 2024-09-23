import json
from fastapi import APIRouter, Response, status

from schemas import SecuredCredentialWithOptions
from schemas.mappings.vcr_credential import VCRCredential
from services import vcr as vcr_service
from services import Verifier

router = APIRouter(prefix="/credentials", tags=["credentials"], redirect_slashes=False)


response_model = {
    "response_model": SecuredCredentialWithOptions,
    "response_model_exclude_none": True,
    "response_model_by_alias": True,
}


@router.get(
    "/{credential_id}",
    status_code=status.HTTP_200_OK,
    response_model=dict,
)
async def get_credentials(credential_id: str):
    """Get credentials"""

    try:
        svc_response = await vcr_service.get_credential(credential_id)
        # TODO: Log the response
        print(svc_response)
        return svc_response
    except Exception as e:
        # TODO: Log the error
        print(e)
        return Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=json.dumps({"error": "There was an error getting the credential"}),
            media_type="application/ld+json",
        )


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
async def issue_credential(secured_credential: SecuredCredentialWithOptions):
    """Issue a new credential"""

    try:
        secured_credential_data = secured_credential.model_dump(
            by_alias=True, exclude_none=True
        )
        
        verifier = Verifier()
        await verifier.verify_secured_document(secured_credential_data['raw_data'].copy())

        vcr_credential = VCRCredential(**secured_credential_data)

        data = vcr_credential.model_dump(by_alias=True, exclude_none=True)
        svc_response = await vcr_service.issue_credential(data)
        # TODO: Log the response
        print(svc_response)
    except Exception as e:
        # TODO: Log the error
        print(e)
        return Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=json.dumps({"error": "There was an error issuing the credential"}),
            media_type="application/json",
        )

    return secured_credential
