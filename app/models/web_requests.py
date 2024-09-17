from typing import Dict, Any
from pydantic import BaseModel, Field
from .options import CredentialTypeOptions, CredentialOptions
from .credential import Credential
from .presentation import Presentation
from .credential_type import CredentialType


class WebBaseModel(BaseModel):
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)


class RegisterCredentialTypeRequest(WebBaseModel):
    credential_type: CredentialType = Field(alias="credentialType")
    options: CredentialTypeOptions = Field()


class RegisterCredentialTypeResponse(WebBaseModel):
    status: bool = Field(example=True)
    credential_type: CredentialType = Field(alias="credentialType")


class StoreCredentialRequest(WebBaseModel):
    verifiable_presentation: Presentation = Field(alias="verifiablePresentation")
    options: CredentialOptions = Field()


class StoreCredentialResponse(WebBaseModel):
    status: bool = Field(example=True)
    replaced: bool = Field(example=False)
    credential: Credential = Field()
