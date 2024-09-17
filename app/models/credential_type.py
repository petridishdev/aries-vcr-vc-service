from typing import List
from app.models import CredentialTypeOptions
from app.models.enums import CredentialFormatEnum, CredentialMappingTypeEnum
from .proof import AuthProof
from pydantic import BaseModel, Field


class Path(BaseModel):
    """Path schema"""

    path: str


class CredentialTopic(BaseModel):
    """Topic schema"""

    type: str = Field(example="registration.registries.ca")
    source_id: Path = Field(
        alias="sourceId", example={"path": "$.credentialSubject.issuedTo.identifier"}
    )


class CredentialMapping(Path):
    """CredentialMapping schema"""

    type: CredentialMappingTypeEnum = Field(example="effective_date")
    name: str = Field(example="effective_date")
    path: str = Field(example="$.validFrom")


class CredentialType(CredentialTypeOptions, BaseModel):
    """CredentialType schema"""

    type: str = Field(example="ExampleCredential")
    format: CredentialFormatEnum = Field(example="vc_di")
    version: str = Field(example="1.0")
    issuer: str = Field(example="did:web:example.com")
    verification_methods: List[str] = Field(
        alias="verificationMethods", example=["did:web:example.com#key-01"]
    )
    topic: CredentialTopic = Field()
    oca_bundle: dict = Field(None, alias="ocaBundle")
    mappings: List[CredentialMapping] = Field(None)
    proof: List[AuthProof] = Field()
