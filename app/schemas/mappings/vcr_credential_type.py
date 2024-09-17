from typing import Any, Dict
from pydantic import model_serializer, BaseModel

from app.enums import CredentialMappingTypeEnum
from ..credential_type import CredentialType
from ..options import CredentialTypeOptions


class BaseModel(BaseModel):
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)


class VCRCredentialType(BaseModel):
    """VCRCredentialType schema"""

    credential_type: CredentialType
    options: CredentialTypeOptions

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        """Serialize the model"""

        model_dump = {
            "format": self.credential_type.format,
            "schema": self.credential_type.type,
            "version": self.credential_type.version,
            "origin_did": self.credential_type.issuer,
            "topic": self.credential_type.topic,
            "raw_data": self.credential_type,
        }

        if self.credential_type.mappings:
            credential = {}
            for mapping in self.credential_type.mappings:
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
                mapping.model_dump(mode="json")
                for mapping in self.credential_type.mappings
            ]

        return model_dump
