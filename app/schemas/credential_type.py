from typing import List

from app.schemas import CredentialMapping, CredentialTopic, CredentialTypeOptions
from app.enums import CredentialFormatEnum
from .proof import AuthProof
from pydantic import BaseModel, Field


class CredentialType(CredentialTypeOptions, BaseModel):
    """CredentialType schema"""
    type: str = Field(example='ExampleCredential')
    format: CredentialFormatEnum = Field(example="vc_di")
    version: str = Field(example='1.0')
    issuer: str = Field(example='did:web:example.com')
    verification_methods: List[str] = Field(alias="verificationMethods", example=['did:web:example.com#key-01'])
    topic: CredentialTopic = Field()
    oca_bundle: dict = Field(None, alias="ocaBundle")
    mappings: List[CredentialMapping] = Field(None)
    proof: List[AuthProof] = Field()
