from typing import Any
from pydantic import model_serializer

from schemas import SecuredCredentialWithOptions


class VCRCredential(SecuredCredentialWithOptions):
    """VCRCredential schema"""

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        """Serialize the model"""

        secured_document = self.secured_document
        options = self.options

        model_dump = {
            "format": options.format.value,
            "schema": options.type,
            "version": options.version,
            "origin_did": secured_document.origin_did,
            "credential_id": options.credential_id,
            "raw_data": self.raw_data,
        }

        return model_dump
