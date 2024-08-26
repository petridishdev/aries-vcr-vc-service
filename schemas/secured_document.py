from typing import Annotated, Generic, TypeVar
from fastapi import Body
from pydantic import BaseModel

SecuredDocumentT = TypeVar("SecuredDocumentT")


class SecuredDocument(BaseModel, Generic[SecuredDocumentT]):
    secured_document: Annotated[
        SecuredDocumentT,
        Body(
            validation_alias="securedDocument",
            serialization_alias="securedDocument",
        ),
    ]
