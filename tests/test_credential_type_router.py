import copy
from fastapi.testclient import TestClient

from tests.data import credential_type_request

from app import app

client = TestClient(app)


def test_register_credential_type():
    """Test register_credential_type"""
    test_data = copy.deepcopy(credential_type_request)
    response = client.post(
        "/credential-types", json=copy.deepcopy(test_data)
    )
    assert response.status_code == 201


def test_register_credential_type_invalid_data():
    """Test register_credential_type with invalid data"""

    test_data = copy.deepcopy(credential_type_request)
    test_data['credentialType'].pop('issuer')
    response = client.post("/credential-types", json={})
    assert response.status_code == 422
    # assert response.json() == {
    #     "detail": [
    #         {
    #             "input": {},
    #             "loc": ["body", "securedDocument"],
    #             "msg": "Field required",
    #             "type": "missing",
    #         },
    #     ]
    # }


def test_register_credential_type_missing():
    """Test register_credential_type with invalid secured_document"""

    test_data = {
        "credentialType": {},
    }

    response = client.post(
        "/credential-types",
        json=test_data,
    )
    assert response.status_code == 422
#     assert response.json() == {
#         "detail": [
#             {
#                 "input": {},
#                 "loc": ["body", "securedDocument", "format"],
#                 "msg": "Field required",
#                 "type": "missing",
#             },
#             {
#                 "input": {},
#                 "loc": ["body", "securedDocument", "type"],
#                 "msg": "Field required",
#                 "type": "missing",
#             },
#             {
#                 "input": {},
#                 "loc": ["body", "securedDocument", "version"],
#                 "msg": "Field required",
#                 "type": "missing",
#             },
#             {
#                 "input": {},
#                 "loc": ["body", "securedDocument", "verificationMethods"],
#                 "msg": "Field required",
#                 "type": "missing",
#             },
#             {
#                 "input": {},
#                 "loc": ["body", "securedDocument", "topic"],
#                 "msg": "Field required",
#                 "type": "missing",
#             },
#             {
#                 "input": {},
#                 "loc": ["body", "securedDocument", "proof"],
#                 "msg": "Field required",
#                 "type": "missing",
#             },
#         ]
#     }


def test_register_credential_type_invalid_topic():
    """Test register_credential_type with invalid topic"""

    test_data = copy.deepcopy(credential_type_request)

    test_data["credentialType"]["topic"] = {
        "type": "registration.registries.ca",
        "sourceId": "invalid_source_id",
    }

    response = client.post(
        "/credential-types",
        json=test_data,
    )
    assert response.status_code == 422
#     assert response.json() == {
#         "detail": [
#             {
#                 "ctx": {
#                     "class_name": "Path",
#                 },
#                 "input": "invalid_source_id",
#                 "loc": ["body", "securedDocument", "topic", "sourceId"],
#                 "msg": "Input should be a valid dictionary or instance of Path",
#                 "type": "model_type",
#             },
#         ]
#     }
