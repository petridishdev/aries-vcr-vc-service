from typing import Dict, Any, List
from pydantic import BaseModel, Field
from .credential import Credential
from .proof import AuthProof


class Presentation(BaseModel):
    context: List[str] = Field(alias="@context", example=[
        "https://www.w3.org/ns/credentials/v2",
        "https://www.w3.org/ns/credentials/examples/v2"
    ])
    type: List[str] = Field(["VerifiablePresentation"])
    verifiable_credential: List[Credential] = Field(alias="verifiableCredential")
    proof: List[AuthProof] = Field()
