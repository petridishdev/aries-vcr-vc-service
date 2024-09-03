from pydantic import BaseModel

from enums import CredentialFormatEnum


class Options(BaseModel):
    """Options schema"""

    format: CredentialFormatEnum
    type: str
    version: str