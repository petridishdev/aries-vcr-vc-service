from typing import Annotated

from fastapi import Body
from schemas import SecuredDocument, SignedCredential, Options


class SecuredCredentialOptions(Options):
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
