topic_spec = {
    "type": "my-registration.city-of-vancouver",
    "sourceId": {"path": "$.path.to.topic.source_id"},
}

effective_date_mapping_spec = {
    "type": "effective_date",
    "name": "test_effective_date",
    "path": "$.path.to.credential.effective_date",
}

expiry_date_mapping_spec = {
    "type": "expiry_date",
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
        expiry_date_mapping_spec,
    ],
}

secured_credential_type_spec = {
    "securedDocument": {
        "format": "vc_di",
        "type": "BCPetroleum&NaturalGasTitle",
        "name": "BC Petroleum & Natural Gas Title",
        "version": "0.0.3",
        "verificationMethods": [
            "did:web:untp.traceability.site:parties:regulators:director-of-petroleum-lands#multikey"
        ],
        "topic": {
            "type": "my-registration.city-of-vancouver",
            "sourceId": {"path": "$.credentialSubject.issuedTo.identifier"},
        },
        "mappings": [
            {"type": "effective_date", "name": "effective_date", "path": "$.validFrom"},
            {"type": "expiry_date", "name": "expiry_date", "path": "$.validUntil"},
            # {
            #     "type": "title_holder",
            #     "name": "title_holder",
            #     "path": "$.credentialSubject.issuedTo.legalName",
            # },
        ],
        "resources": [
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

secured_credential_spec = {
    "options": {
        "format": "vc_di",
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "0.0.3",
        "credentialId": "203296ac-6d8f-4988-9d7f-d23d3ca36db4"
    },
    "securedDocument": {
        "@context": ["https://www.w3.org/ns/credentials/v2"],
        "type": ["VerifiableCredential", "BCPetroleum&NaturalGasTitle"],
        "id": "https://orgbook.devops.gov.bc.ca/entities/81011e4c-979d-436c-b98c-9412daafd5de/credentials/203296ac-6d8f-4988-9d7f-d23d3ca36db4",
        "issuer": {
            "id": "did:web:untp.traceability.site:parties:regulators:director-of-petroleum-lands#multikey"
        },
        "validFrom": "2024-08-12T05:44:20+00:00",
        "validUntil": "2025-08-12T05:44:20+00:00",
        "credentialSubject": {
            "issuedTo": {
                "id": "https://orgbook.gov.bc.ca/entity/81011e4c-979d-436c-b98c-9412daafd5de",
                "legalName": "PACIFIC CANBRIAM ENERGY LIMITED",
                "identifier": "81011e4c-979d-436c-b98c-9412daafd5de",
            }
        },
        "proof": [
            {
                "type": "DataIntegrityProof",
                "cryptosuite": "eddsa-jcs-2022",
                "verificationMethod": "did:web:untp.traceability.site:parties:regulators:director-of-petroleum-lands#multikey",
                "proofPurpose": "assertionMethod",
                "proofValue": "z2Nr9eDUfBzircv484R3u7vzdxARh5D8vsbj4ohFRQZhkq2PTdJ9YsLfF18mafaPMtchV5EefmovvFoFbFNmLqrWW",
            }
        ],
    }
}
