from enums import CredentialMappingTypeEnum
from schemas import Path

class CredentialMapping(Path):
    """CredentialMapping schema"""

    type: CredentialMappingTypeEnum
    name: str