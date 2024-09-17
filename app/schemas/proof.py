from pydantic import BaseModel, Field


class DataIntegrityProof(BaseModel):
    """DataIntegrityProof schema"""

    type: str = Field("DataIntegrityProof")
    cryptosuite: str = Field("eddsa-jcs-2022")
    verificationMethod: str = Field(example="did:web:example.com#key-01")
    proofPurpose: str = Field(example="assertionMethod")
    proofValue: str = Field()


class AuthProof(BaseModel):
    """DataIntegrityProof schema"""

    type: str = Field("DataIntegrityProof")
    cryptosuite: str = Field("eddsa-jcs-2022")
    verificationMethod: str = Field(example="did:web:example.com#key-01")
    proofPurpose: str = Field(example="authentication")
    proofValue: str = Field()


class AssertionProof(BaseModel):
    """DataIntegrityProof schema"""

    type: str = Field("DataIntegrityProof")
    cryptosuite: str = Field("eddsa-jcs-2022")
    verificationMethod: str = Field(example="did:web:example.com#key-01")
    proofPurpose: str = Field(example="assertionMethod")
    proofValue: str = Field()
