from pydantic import BaseModel


class DataIntegrityProof(BaseModel):
    type: str = "DataIntegrityProof"
    cryptosuite: str
    verificationMethod: str
    proofPurpose: str
    proofValue: str