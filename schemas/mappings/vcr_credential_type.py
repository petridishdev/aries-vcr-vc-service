from typing import Any
from pydantic import model_serializer

from enums import CredentialMappingTypeEnum
from schemas import SecuredDocument, SignedCredentialType


class VCRCredentialType(SecuredDocument[SignedCredentialType]):
    """VCRCredentialType schema"""

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        """Serialize the model"""

        secured_document = self.secured_document

        model_dump = {
            "format": secured_document.format.value,
            "schema": secured_document.type,
            "version": secured_document.version,
            "origin_did": secured_document.origin_did,
            "topic": secured_document.topic.model_dump(mode="json"),
            "raw_data": self.raw_data,
        }

        if secured_document.mappings:
            credential = {}
            for mapping in secured_document.mappings:
                if mapping.type in (
                    CredentialMappingTypeEnum.EFFECTIVE_DATE,
                    CredentialMappingTypeEnum.REVOKED_DATE,
                ):
                    credential[mapping.type.value] = mapping.model_dump(
                        exclude={"type"}
                    )

            if credential:
                model_dump["credential"] = credential

            model_dump["mappings"] = [
                mapping.model_dump(mode="json") for mapping in secured_document.mappings
            ]

        return model_dump
