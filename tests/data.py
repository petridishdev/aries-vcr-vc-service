TEST_DID = "did:web:example.com"
TEST_KID = f'{TEST_DID}#key-01'
TEST_CREDENTIAL_ID = "https://orgbook.devops.gov.bc.ca/entities/81011e4c-979d-436c-b98c-9412daafd5de/credentials/203296ac-6d8f-4988-9d7f-d23d3ca36db4"
TEST_CREDENTIAL_TYPE = "ExampleCredential"

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
    "type": TEST_CREDENTIAL_TYPE,
    "version": "1.0",
    "verificationMethods": [TEST_KID],
    "topic": topic_spec,
    "mappings": [
        effective_date_mapping_spec,
        expiry_date_mapping_spec,
    ],
}

credential_type_request = {
    "credentialType": {
        "type": TEST_CREDENTIAL_TYPE,
        "format": "vc_di",
        "version": "0.0.3",
        "issuer": TEST_DID,
        "verificationMethods": [
            TEST_KID
        ],
        "topic": {
            "type": "my-registration.city-of-vancouver",
            "sourceId": {"path": "$.credentialSubject.identifier"},
        },
        "ocaBundle": {},
        "mappings": [
            {"type": "effective_date", "name": "effective_date", "path": "$.validFrom"},
            {"type": "expiry_date", "name": "expiry_date", "path": "$.validUntil"}
        ],
        "proof": [
            {
                "type": "DataIntegrityProof",
                "cryptosuite": "eddsa-jcs-2022",
                "verificationMethod": TEST_KID,
                "proofPurpose": "authentication",
                "proofValue": "z17CzsxiNiugmX9CYseEkoXxjMqBDxyasiwWwZ58AD5ctKJLjSeoEmSBvj5VVxzATFfpwKdfRmjqLn2wRMhb9jHV",
            }
        ],
    },
    "options": {"issuerId": TEST_DID}
}

secured_credential_spec = {
    "options": {
        "format": "vc_di",
        "type": TEST_CREDENTIAL_TYPE,
        "version": "0.0.3",
        "credentialId": TEST_CREDENTIAL_ID,
        "issuedId": TEST_DID
    },
    "verifiablePresentation": {
        "@context": ["https://www.w3.org/ns/credentials/v2"],
        "type": ["VerifiablePresentation"],
        "verifiableCredential":[{"@context": ["https://www.w3.org/ns/credentials/v2"],
        "type": ["VerifiableCredential", TEST_CREDENTIAL_TYPE],
        "id": TEST_CREDENTIAL_ID,
        "issuer": {
            "id": TEST_DID
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
                "verificationMethod": TEST_KID,
                "proofPurpose": "assertionMethod",
                "proofValue": "z2Nr9eDUfBzircv484R3u7vzdxARh5D8vsbj4ohFRQZhkq2PTdJ9YsLfF18mafaPMtchV5EefmovvFoFbFNmLqrWW",
            }
        ]}],
    },
}
