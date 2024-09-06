from typing import Annotated
from fastapi import Body
from pydantic import BaseModel
from schemas import Signed


class SignedCredential(Signed, BaseModel):
    """SignedCredential schema"""

    context: Annotated[
        list[str], Body(validation_alias="@context", serialization_alias="@context")
    ]
    id: str
    type: list[str]
    issuer: str | dict
    validFrom: str
    validUntil: str
    name: str | dict | None = None
    description: str | dict | None = None
    credentialSubject: dict
