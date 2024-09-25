from typing import Annotated
from pydantic import BaseModel, Field


class Issuer(BaseModel):
    """Issuer schema"""

    name: str
    did: Annotated[str, Field(validation_alias="id")]
    abbreviation: str | None = ""
    email: str | None = ""
    url: str | None = ""
