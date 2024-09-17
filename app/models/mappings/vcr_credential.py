from typing import Any, Dict
from pydantic import model_serializer, BaseModel
from ..credential import Credential
from ..options import CredentialOptions


class EfficientBaseModel(BaseModel):
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        return super().model_dump(by_alias=True, exclude_none=True, **kwargs)


class VCRCredential(EfficientBaseModel):
    """VCRCredential schema"""

    credential: Credential
    options: CredentialOptions

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        """Serialize the model"""

        model_dump = {
            "format": self.options.credential_format,
            "schema": self.options.credential_type,
            "version": self.options.credential_version,
            "origin_did": self.credential.issuer["id"],
            "credential_id": self.credential.id,
            "raw_data": self.credential,
        }

        return model_dump
