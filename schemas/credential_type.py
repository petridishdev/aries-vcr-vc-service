from typing import Annotated

from fastapi import Body
from schemas import CredentialMapping, CredentialTopic, Options
from pydantic import BaseModel


class CredentialType(Options, BaseModel):
    """CredentialType schema"""

    verification_methods: Annotated[
        list[str],
        Body(
            validation_alias="verificationMethods",
            serialization_alias="verificationMethods",
        ),
    ]
    oca_bundle: Annotated[dict | None, Body(validation_alias="ocaBundle")] = None
    topic: CredentialTopic
    mappings: list[CredentialMapping] | None = None
