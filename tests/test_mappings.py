from schemas.mappings import VCRCredentialType

from tests.data import credential_type_spec


def test_valid_vcr_credential_type_output():
    """Test the output of the VCRCredentialType model."""

    vcr_credential_type = VCRCredentialType(**credential_type_spec)
    vcr_credential_type_output = vcr_credential_type.model_dump(
        by_alias=True, exclude_none=True
    )

    assert vcr_credential_type_output == {
        "format": "vc_di",
        "schema": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "origin_did": "did:key:for:issuer",
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
        "mappings": [
            {
                "type": "effective_date",
                "name": "test_effective_date",
                "path": "$.path.to.credential.effective_date",
            },
            {
                "type": "revoked_date",
                "name": "test_expiry_date",
                "path": "$.path.to.credential.expiry_date",
            },
        ],
        "credential": {
            "effective_date": {
                "name": "test_effective_date",
                "path": "$.path.to.credential.effective_date",
            },
            "revoked_date": {
                "name": "test_expiry_date",
                "path": "$.path.to.credential.expiry_date",
            },
        },
    }