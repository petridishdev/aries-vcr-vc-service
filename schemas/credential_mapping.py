from enums import CredentialMappingTypeEnum
from schemas import PathBase

class CredentialMapping(PathBase):
    """CredentialMapping schema"""

    type: CredentialMappingTypeEnum
    name: str