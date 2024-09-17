from typing import Dict, Any
from pydantic import BaseModel, Field
from app.enums import CredentialFormatEnum


class BaseModel(BaseModel):
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)


class CredentialTypeOptions(BaseModel):
    """Options schema"""

    issuerId: str = Field(example="did:web:example.com")


class CredentialOptions(BaseModel):
    """Options schema"""

    issuer_id: str = Field(alias="issuerId", example="did:web:example.com")
    credential_id: str = Field(
        alias="credentialId", example="https://example.com/credentials/123"
    )
    credential_type: str = Field(alias="credentialType", example="ExampleCredential")
    credential_version: str = Field(alias="credentialVersion", example="1.0")
    credential_format: CredentialFormatEnum = Field(
        alias="credentialFormat", example="vc_di"
    )
