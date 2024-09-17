from enum import Enum


class CredentialMappingTypeEnum(str, Enum):
    """CredentialMappingAttribute enum"""

    EFFECTIVE_DATE = "effective_date"
    EXPIRY_DATE = "expiry_date"
    REVOKED_DATE = "revoked_date"
