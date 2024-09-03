from pydantic import BaseModel

from schemas import DataIntegrityProof


class Signed(BaseModel):
    """Signed schema"""

    proof: list[DataIntegrityProof]

    @property
    def origin_did(self) -> str:
        return self.proof[0].verificationMethod.split("#")[0]