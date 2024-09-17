from app.enums import CredentialMappingTypeEnum
from app.schemas import Path


class CredentialMapping(Path):
    """CredentialMapping schema"""

    type: CredentialMappingTypeEnum
    name: str
