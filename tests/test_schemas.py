import pytest

from pydantic import ValidationError

from schemas import CredentialMapping, CredentialTopic, CredentialType

from tests.data import credential_type_spec, topic_spec, effective_date_mapping_spec


def test_valid_credential_topic_schema():
    """Test valid CredentialTopic schema"""

    test_data = topic_spec.copy()

    credential_topic = CredentialTopic(**test_data)

    assert credential_topic.model_dump(exclude_none=True) == {
        "type": test_data.get("type"),
        "source_id": test_data.get("sourceId"),
    }


def test_invalid_credential_topic_schema_missing_type():
    """Test invalid CredentialTopic schema missing type"""

    test_data = topic_spec.copy()
    del test_data["type"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_topic_schema_missing_source_id():
    """Test invalid CredentialTopic schema missing source_id"""

    test_data = topic_spec.copy()
    del test_data["sourceId"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "sourceId" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_topic_schema_missing_source_id_path():
    """Test invalid CredentialTopic schema missing source_id path"""

    test_data = {
        **topic_spec.copy(),
        "sourceId": {},
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_topic_schema_invalid_source_id():
    """Test invalid CredentialTopic schema invalid source_id"""

    test_data = {
        **topic_spec.copy(),
        "sourceId": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**test_data)

    errors = exc_info.value.errors()[0]

    assert (
        errors.get("msg")
        == "Input should be a valid dictionary or instance of PathBase"
    )
    assert "sourceId" in errors.get("loc")
    assert errors.get("type") == "model_type"


def test_invalid_credential_topic_schema_invalid_source_id_path():
    """Test invalid CredentialTopic schema invalid source_id path"""

    test_data = {
        **topic_spec.copy(),
        "sourceId": {"path": 123},
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid string"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "string_type"


def test_valid_credential_mapping_schema():
    """Test valid CredentialMapping schema"""

    test_data = effective_date_mapping_spec.copy()

    credential_mapping = CredentialMapping(**test_data)

    assert credential_mapping.model_dump() == test_data


def test_invalid_credential_mapping_schema_missing_path():
    """Test invalid CredentialMapping schema missing path"""

    test_data = effective_date_mapping_spec.copy()
    del test_data["path"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_mapping_schema_missing_type():
    """Test invalid CredentialMapping schema missing type"""

    test_data = effective_date_mapping_spec.copy()
    del test_data["type"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_mapping_schema_missing_name():
    """Test invalid CredentialMapping schema missing name"""

    test_data = effective_date_mapping_spec.copy()
    del test_data["name"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "name" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_mapping_schema_invalid_path():
    """Test invalid CredentialMapping schema invalid path"""

    test_data = {
        **effective_date_mapping_spec.copy(),
        "path": 123,
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid string"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "string_type"


def test_invalid_credential_mapping_schema_invalid_mapping_type():
    """Test invalid CredentialMapping schema invalid mapping"""

    test_data = {
        **effective_date_mapping_spec.copy(),
        "type": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be 'effective_date' or 'revoked_date'"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "enum"


def test_valid_credential_type_schema():
    """Test valid CredentialType schema"""

    credential_type = CredentialType(**credential_type_spec)
    credential_type_output = credential_type.model_dump(exclude_none=True)

    assert credential_type_output == {
        "format": str(credential_type_spec.get("format")),
        "type": credential_type_spec.get("type"),
        "version": credential_type_spec.get("version"),
        "verification_methods": credential_type_spec.get("verificationMethods"),
        "topic": {
            "type": topic_spec.get("type"),
            "source_id": topic_spec.get("sourceId"),
        },
        "mappings": credential_type_spec.get("mappings"),
    }


def test_valid_credential_type_schema_no_mappings():
    """Test valid CredentialType schema with no mappings"""

    test_data = credential_type_spec.copy()
    del test_data["mappings"]

    credential_type = CredentialType(**test_data)
    credential_type_output = credential_type.model_dump(exclude_none=True)

    assert credential_type_output == {
        "format": str(credential_type_spec.get("format")),
        "type": credential_type_spec.get("type"),
        "version": credential_type_spec.get("version"),
        "verification_methods": credential_type_spec.get("verificationMethods"),
        "topic": {
            "type": topic_spec.get("type"),
            "source_id": topic_spec.get("sourceId"),
        },
    }
    assert "mappings" not in credential_type_output


def test_valid_credential_type_schema_empty_mappings():
    """Test valid CredentialType schema with empty mappings"""

    test_data = credential_type_spec.copy()
    test_data["mappings"] = []

    credential_type = CredentialType(**test_data)
    credential_type_output = credential_type.model_dump(exclude_none=True)

    assert credential_type_output == {
        "format": str(credential_type_spec.get("format")),
        "type": credential_type_spec.get("type"),
        "version": credential_type_spec.get("version"),
        "verification_methods": credential_type_spec.get("verificationMethods"),
        "topic": {
            "type": topic_spec.get("type"),
            "source_id": topic_spec.get("sourceId"),
        },
        "mappings": [],
    }


def test_invalid_credential_type_schema_missing_format():
    """Test invalid CredentialType schema missing format"""

    test_data = credential_type_spec.copy()
    del test_data["format"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "format" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_type():
    """Test invalid CredentialType schema missing type"""

    test_data = credential_type_spec.copy()
    del test_data["type"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_version():
    """Test invalid CredentialType schema missing version"""

    test_data = credential_type_spec.copy()
    del test_data["version"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "version" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_verification_methods():
    """Test invalid CredentialType schema missing verification_methods"""

    test_data = credential_type_spec.copy()
    del test_data["verificationMethods"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "verificationMethods" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_topic():
    """Test invalid CredentialType schema missing topic"""

    test_data = credential_type_spec.copy()
    del test_data["topic"]

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "topic" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_invalid_format():
    """Test invalid CredentialType schema invalid format"""

    test_data = {
        **credential_type_spec.copy(),
        "format": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be 'vc_di' or 'anoncreds'"
    assert "format" in errors.get("loc")
    assert errors.get("type") == "enum"


def test_invalid_credential_type_schema_invalid_verification_methods():
    """Test invalid CredentialType schema invalid verification_methods"""

    test_data = {
        **credential_type_spec.copy(),
        "verificationMethods": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid list"
    assert "verificationMethods" in errors.get("loc")
    assert errors.get("type") == "list_type"


def test_invalid_credential_type_schema_invalid_oca_bundle():
    """Test invalid CredentialType schema invalid oca_bundle"""

    test_data = {
        **credential_type_spec.copy(),
        "ocaBundle": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid dictionary"
    assert "ocaBundle" in errors.get("loc")
    assert errors.get("type") == "dict_type"


def test_invalid_credential_type_schema_invalid_mappings():
    """Test invalid CredentialType schema invalid mappings"""

    test_data = {
        **credential_type_spec.copy(),
        "mappings": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**test_data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid list"
    assert "mappings" in errors.get("loc")
    assert errors.get("type") == "list_type"
