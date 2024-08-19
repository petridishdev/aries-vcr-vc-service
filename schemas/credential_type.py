from enums import CredentialFormatEnum
from schemas import CredentialMapping, CredentialTopic
from pydantic import BaseModel


class CredentialType(BaseModel):
    """CredentialType schema"""

    format: CredentialFormatEnum
    type: str
    version: str
    verification_methods: list[str]
    oca_bundle: dict | None = None
    topic: CredentialTopic
    mappings: list[CredentialMapping] | None = None
