from typing import Annotated
from fastapi import Body
from pydantic import BaseModel
from schemas import PathBase as Path


class CredentialTopic(BaseModel):
    """Topic schema"""

    type: str
    source_id: Annotated[
        Path,
        Body(
            alias="sourceId",
            validation_alias="sourceId",
            serialization_alias="sourceId",
        ),
    ]
