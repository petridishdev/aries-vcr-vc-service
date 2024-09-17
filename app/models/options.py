from typing import Dict, Any
from pydantic import BaseModel, Field
from app.models.enums import CredentialFormatEnum


class CredentialTypeOptions(BaseModel):
    """Options schema"""

    issuer_id: str = Field(alias="issuerId", example="did:web:example.com")


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
