from typing import Any
from pydantic import model_serializer

from enums import CredentialMappingTypeEnum
from schemas import SecuredDocument, SignedCredentialType


class VCRCredentialType(SecuredDocument[SignedCredentialType]):
    """VCRCredentialType schema"""

    raw_data: SecuredDocument[SignedCredentialType] = None

    def __init__(self, **data: SecuredDocument[SignedCredentialType]) -> None:
        super().__init__(**data)

        self.raw_data = data

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        """Serialize the model"""

        secured_document = self.secured_document

        model_dump = {
            "format": secured_document.format.value,
            "topic": secured_document.topic.model_dump(mode="json"),
            "schema": secured_document.type,
            "version": secured_document.version,
            "origin_did": secured_document.verification_methods[0],
        }

        if secured_document.mappings:
            credential = {}
            for mapping in secured_document.mappings:
                if mapping.type in CredentialMappingTypeEnum:
                    credential[mapping.type.value] = mapping.model_dump(
                        exclude={"type"}
                    )

            if credential:
                model_dump["credential"] = credential

            model_dump["mappings"] = [
                mapping.model_dump(mode="json") for mapping in secured_document.mappings
            ]

        model_dump["raw_data"] = self.raw_data

        return model_dump
