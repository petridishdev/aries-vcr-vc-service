from pydantic import BaseModel


class Path(BaseModel):
    """Path schema"""

    path: str
