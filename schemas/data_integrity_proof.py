from pydantic import BaseModel


class DataIntegrityProof(BaseModel):
    """DataIntegrityProof schema"""

    type: str = "DataIntegrityProof"
    cryptosuite: str
    verificationMethod: str
    proofPurpose: str
    proofValue: str