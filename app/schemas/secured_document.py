from typing import Annotated, Generic, TypeVar
from fastapi import Body
from pydantic import BaseModel

SecuredDocumentT = TypeVar("SecuredDocumentT")


class SecuredDocument(BaseModel, Generic[SecuredDocumentT]):
    """SecuredDocument schema"""

    raw_data: dict = None
    secured_document: Annotated[
        SecuredDocumentT,
        Body(
            validation_alias="securedDocument",
            serialization_alias="securedDocument",
        ),
    ]

    def __init__(self, **data: SecuredDocumentT) -> None:
        super().__init__(**data)

        self.raw_data = data.get("securedDocument")
