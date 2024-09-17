from typing import List, Union
from pydantic import BaseModel, Field
from .proof import AssertionProof


class Issuer(BaseModel):
    id: str = Field(example="did:web:example.com")
    name: str = Field(example="Example Issuer")
    description: str = Field(example="An example issuer for testing.")


class RenderMethod(BaseModel):
    type: str = Field(example="BitstringStatusListEntry")
    statusPurpose: str = Field(example="revocation")
    statusListIndex: str = Field(example="4892781")
    statusListCredential: str = Field(
        example="https://example.com/credentials/status/123"
    )


class Credential(BaseModel):
    context: List[str] = Field(alias="@context", example=[
        "https://www.w3.org/ns/credentials/v2",
        "https://www.w3.org/ns/credentials/examples/v2"
    ])
    type: List[str] = Field(["VerifiableCredential", "ExampleCredential"])
    id: str = Field(example="https://example.com/credentials/123")
    issuer: Issuer = Field()
    validFrom: str = Field(None, example="2024-01-01T00:00:00Z")
    validUntil: str = Field(None, example="2025-01-01T00:00:00Z")
    name: Union[str, dict] = Field(None, example="Example Credential")
    description: Union[str, dict] = Field(
        None, example="An example credential for testing."
    )
    credential_subject: Union[dict, List[dict]] = Field(
        alias="credentialSubject", example={"name": "Alice"}
    )
    render_method: List[RenderMethod] = Field(None, alias="renderMethod")
    proof: List[AssertionProof] = Field()
