from typing import Dict, Any, List
from pydantic import BaseModel, Field
from .credential import Credential
from .proof import AuthProof


class BaseModel(BaseModel):
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)


class Presentation(BaseModel):
    context: List[str] = Field(["https://www.w3.org/ns/credentials/v2"])
    type: List[str] = Field(["VerifiablePresentation"])
    verifiable_credential: List[Credential] = Field(alias="verifiableCredential")
    proof: List[AuthProof] = Field()
