from pydantic import BaseModel

from schemas import DataIntegrityProof


class Signed(BaseModel):
    """Signed schema"""

    proof: list[DataIntegrityProof] | list | None = None
