from pydantic import model_serializer
from schemas import CredentialType, DataIntegrityProof


class SignedCredentialType(CredentialType):
    """SignedCredentialType schema"""

    proof: list[DataIntegrityProof] | list | None = None