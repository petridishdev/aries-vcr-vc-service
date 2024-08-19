from pydantic import BaseModel


class PathBase(BaseModel):
    """PathBase schema"""

    path: str
