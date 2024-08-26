topic_spec = {
    "type": "registration.registries.ca",
    "sourceId": {"path": "$.path.to.topic.source_id"},
}

effective_date_mapping_spec = {
    "type": "effective_date",
    "name": "test_effective_date",
    "path": "$.path.to.credential.effective_date",
}

revoked_date_mapping_spec = {
    "type": "revoked_date",
    "name": "test_expiry_date",
    "path": "$.path.to.credential.expiry_date",
}

credential_type_spec = {
    "format": "vc_di",
    "type": "BCPetroleum&NaturalGasTitle",
    "version": "1.0",
    "verificationMethods": ["did:key:for:issuer"],
    "topic": topic_spec,
    "mappings": [
        effective_date_mapping_spec,
        revoked_date_mapping_spec,
    ],
}

signed_credential_type_spec = {
    "securedDocument": {
        "format": "vc_di",
        "type": "BCPetroleum&NaturalGasTitle",
        "name": "BC Petroleum & Natural Gas Title",
        "version": "0.1",
        "verificationMethods": [
            "did:web:untp.traceability.site:parties:regulators:director-of-petroleum-lands#multikey"
        ],
        "topic": {
            "type": "registration.registries.ca",
            "sourceId": {"path": "$.credentialSubject.issuedTo.identifier"},
        },
        "mappings": [
            {"type": "effective_date", "name": "effective_date", "path": "$.validFrom"},
            {"type": "revoked_date", "name": "revoked_date", "path": "$.validUntil"},
            # {
            #     "type": "title_holder",
            #     "name": "title_holder",
            #     "path": "$.credentialSubject.issuedTo.legalName",
            # },
        ],
        "ressources": [
            {
                "type": "OverlayCaptureBundle",
                "id": "https://opsecid.github.io/orgbook-registrations/credentials/BCPetroleum&NaturalGasTitle/0.1/OCABundle.json",
                "digest": "",
            },
            {"type": "JsonSchema", "id": "", "digest": ""},
            {"type": "JsonLDContext", "id": "", "digest": ""},
        ],
        "proof": [
            {
                "type": "DataIntegrityProof",
                "cryptosuite": "eddsa-jcs-2022",
                "verificationMethod": "did:web:untp.traceability.site:parties:regulators:director-of-petroleum-lands#multikey",
                "proofPurpose": "authentication",
                "proofValue": "z17CzsxiNiugmX9CYseEkoXxjMqBDxyasiwWwZ58AD5ctKJLjSeoEmSBvj5VVxzATFfpwKdfRmjqLn2wRMhb9jHV",
            }
        ],
    }
}
