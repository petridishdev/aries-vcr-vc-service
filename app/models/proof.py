from pydantic import BaseModel, Field


class DataIntegrityProof(BaseModel):
    """DataIntegrityProof schema"""

    type: str = Field("DataIntegrityProof")
    cryptosuite: str = Field("eddsa-jcs-2022")
    verificationMethod: str = Field(example="did:web:example.com#key-01")
    proofValue: str = Field()


class AuthProof(DataIntegrityProof):
    """DataIntegrityProof schema"""

    proofPurpose: str = Field(example="authentication")


class AssertionProof(DataIntegrityProof):
    """DataIntegrityProof schema"""

    proofPurpose: str = Field(example="assertionMethod")
