from pydantic import BaseModel
from schemas import PathBase as Path


class CredentialTopic(BaseModel):
    """Topic schema"""

    type: str
    source_id: Path
