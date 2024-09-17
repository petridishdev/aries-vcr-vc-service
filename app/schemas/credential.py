from typing import Dict, Any, List, Union
from pydantic import BaseModel, Field
from .proof import AssertionProof


class BaseModel(BaseModel):
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)


class Credential(BaseModel):
    context: List[str] = Field(["https://www.w3.org/ns/credentials/v2"])
    type: List[str] = Field(["VerifiableCredential", "ExampleCredential"])
    id: str = Field(example="https://example.com/credentials/123")
    issuer: dict = Field({"id": "did:web:example.com"})
    credential_subject: Union[dict, List[dict]] = Field(alias="credentialSubject")
    proof: List[AssertionProof] = Field()
