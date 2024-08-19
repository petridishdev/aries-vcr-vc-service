from enum import Enum


class CredentialFormatEnum(str, Enum):
    """CredentialFormat enum"""

    VC_DI = "vc_di"
    ANONCREDS = "anoncreds"
