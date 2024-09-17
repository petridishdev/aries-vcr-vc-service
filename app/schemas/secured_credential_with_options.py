from typing import Annotated

from fastapi import Body
from app.schemas import SecuredDocument, SignedCredential, CredentialOptions


class SecuredCredentialOptions(CredentialOptions):
    """SecuredCredentialOptions schema"""

    credential_id: Annotated[
        str,
        Body(
            validation_alias="credentialId",
            serialization_alias="credentialId",
        ),
    ]


class SecuredCredentialWithOptions(SecuredDocument[SignedCredential]):
    """SecuredCredentialWithOptions schema"""

    options: SecuredCredentialOptions
