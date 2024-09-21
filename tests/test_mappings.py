import copy
from schemas.mappings import VCRCredentialType

from tests.data import secured_credential_type_spec


def test_valid_vcr_credential_type_output():
    """Test the output of the VCRCredentialType model."""

    test_data = copy.deepcopy(secured_credential_type_spec)

    vcr_credential_type = VCRCredentialType(**test_data)
    vcr_credential_type_output = vcr_credential_type.model_dump(
        by_alias=True, exclude_none=True
    )

    assert vcr_credential_type_output == {
        "format": "vc_di",
        "schema": "BCPetroleum&NaturalGasTitle",
        "version": "0.0.3",
        "origin_did": "did:web:untp.traceability.site:parties:regulators:director-of-petroleum-lands",
        "topic": {
            "type": "my-registration.city-of-vancouver",
            "source_id": {"path": "$.credentialSubject.issuedTo.identifier"},
        },
        "mappings": [
            {
                "type": "effective_date",
                "name": "effective_date",
                "path": "$.validFrom",
            },
            {
                "type": "expiry_date",
                "name": "expiry_date",
                "path": "$.validUntil",
            },
        ],
        "credential": {
            "effective_date": {
                "name": "effective_date",
                "path": "$.validFrom",
            },
            # "revoked_date": {
            #     "name": "revoked_date",
            #     "path": "$.validUntil",
            # },
        },
        "raw_data": test_data.get("securedDocument"),
    }
