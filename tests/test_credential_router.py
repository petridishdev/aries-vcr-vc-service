import copy
from fastapi.testclient import TestClient
import pytest

from tests.data import secured_credential_type_spec, secured_credential_spec

from main import app

client = TestClient(app)


@pytest.mark.skip
def test_issue_credential():
    """Test issue_credential"""

    response = client.post(
        "/credential-types/", json=copy.deepcopy(secured_credential_type_spec)
    )
    print(response.json())
    assert response.status_code == 201

    response = client.post("/credentials/", json=copy.deepcopy(secured_credential_spec))
    assert response.status_code == 201


def test_register_credential_type_invalid_data():
    """Test register_credential_type wi th invalid data"""

    response = client.post("/credential-types/", json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": {},
                "loc": ["body", "securedDocument"],
                "msg": "Field required",
                "type": "missing",
            },
        ]
    }
