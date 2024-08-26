from typing import Any
from pydantic import model_serializer

from enums import CredentialMappingTypeEnum
from schemas import CredentialType


class VCRCredentialType(CredentialType):
    """VCRCredentialType schema"""

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        """Serialize the model"""

        model_dump = {
            "format": self.format,
            "topic": self.topic.model_dump(),
            "schema": self.type,
            "version": self.version,
            "origin_did": self.verification_methods[0],
        }

        if self.mappings:
            credential = {}
            for mapping in self.mappings:
                if mapping.type in CredentialMappingTypeEnum:
                    credential[mapping.type] = mapping.model_dump(exclude={"type"})

            if credential:
                model_dump["credential"] = credential

            model_dump["mappings"] = [mapping.model_dump() for mapping in self.mappings]

        return model_dump
