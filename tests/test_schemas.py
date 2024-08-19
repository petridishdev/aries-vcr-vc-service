from pydantic import ValidationError
import pytest

from enums import CredentialMappingTypeEnum
from enums.credential_format import CredentialFormatEnum
from schemas import CredentialMapping, CredentialTopic, CredentialType


def test_valid_credential_topic_schema():
    """Test valid CredentialTopic schema"""

    data = {"type": "test-type", "source_id": {"path": "$.path.to.topic.source_id"}}

    credential_topic = CredentialTopic(**data)

    assert credential_topic.model_dump() == data


def test_invalid_credential_topic_schema_missing_type():
    """Test invalid CredentialTopic schema missing type"""

    data = {"source_id": {"path": "$.path.to.topic.source_id"}}

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_topic_schema_missing_source_id():
    """Test invalid CredentialTopic schema missing source_id"""

    data = {"type": "test-type"}

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "source_id" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_topic_schema_missing_source_id_path():
    """Test invalid CredentialTopic schema missing source_id path"""

    data = {"type": "test-type", "source_id": {}}

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_topic_schema_invalid_source_id():
    """Test invalid CredentialTopic schema invalid source_id"""

    data = {"type": "test-type", "source_id": "invalid"}

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**data)

    errors = exc_info.value.errors()[0]

    assert (
        errors.get("msg")
        == "Input should be a valid dictionary or instance of PathBase"
    )
    assert "source_id" in errors.get("loc")
    assert errors.get("type") == "model_type"


def test_invalid_credential_topic_schema_invalid_source_id_path():
    """Test invalid CredentialTopic schema invalid source_id path"""

    data = {"type": "test-type", "source_id": {"path": 123}}

    with pytest.raises(ValidationError) as exc_info:
        CredentialTopic(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid string"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "string_type"


def test_valid_credential_mapping_schema():
    """Test valid CredentialMapping schema"""

    data = {
        "path": "$.path.to.credential.effective_date",
        "type": CredentialMappingTypeEnum.EFFECTIVE_DATE,
        "name": "test_effective_date",
    }

    credential_mapping = CredentialMapping(**data)

    assert credential_mapping.model_dump() == data


def test_invalid_credential_mapping_schema_missing_path():
    """Test invalid CredentialMapping schema missing path"""

    data = {
        "type": CredentialMappingTypeEnum.EFFECTIVE_DATE,
        "name": "test_effective_date",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_mapping_schema_missing_type():
    """Test invalid CredentialMapping schema missing type"""

    data = {
        "path": "$.path.to.credential.effective_date",
        "name": "test_effective_date",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_mapping_schema_missing_name():
    """Test invalid CredentialMapping schema missing name"""

    data = {
        "path": "$.path.to.credential.effective_date",
        "type": CredentialMappingTypeEnum.EFFECTIVE_DATE,
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "name" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_mapping_schema_invalid_path():
    """Test invalid CredentialMapping schema invalid path"""

    data = {
        "path": 123,
        "type": CredentialMappingTypeEnum.EFFECTIVE_DATE,
        "name": "test_effective_date",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid string"
    assert "path" in errors.get("loc")
    assert errors.get("type") == "string_type"


def test_invalid_credential_mapping_schema_invalid_mapping():
    """Test invalid CredentialMapping schema invalid mapping"""

    data = {
        "path": "$.path.to.credential.effective_date",
        "type": "invalid",
        "name": "test_effective_date",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialMapping(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be 'effective_date' or 'expiry_date'"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "enum"


def test_valid_credential_type_schema():
    """Test valid CredentialType schema"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
        "mappings": [
            {
                "type": CredentialMappingTypeEnum.EFFECTIVE_DATE,
                "name": "test_effective_date",
                "path": "$.path.to.credential.effective_date",
            }
        ],
    }

    credential_type = CredentialType(**data)

    assert credential_type.model_dump(exclude_none=True) == data


def test_valid_credential_type_schema_no_mappings():
    """Test valid CredentialType schema with no mappings"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    credential_type = CredentialType(**data)

    assert credential_type.model_dump(exclude_none=True) == data


def test_valid_credential_type_schema_empty_mappings():
    """Test valid CredentialType schema with empty mappings"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
        "mappings": [],
    }

    credential_type = CredentialType(**data)

    assert credential_type.model_dump(exclude_none=True) == data


def test_invalid_credential_type_schema_missing_format():
    """Test invalid CredentialType schema missing format"""

    data = {
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "format" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_type():
    """Test invalid CredentialType schema missing type"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "type" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_version():
    """Test invalid CredentialType schema missing version"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "version" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_verification_methods():
    """Test invalid CredentialType schema missing verification_methods"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "verification_methods" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_missing_topic():
    """Test invalid CredentialType schema missing topic"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Field required"
    assert "topic" in errors.get("loc")
    assert errors.get("type") == "missing"


def test_invalid_credential_type_schema_invalid_format():
    """Test invalid CredentialType schema invalid format"""

    data = {
        "format": "invalid",
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be 'vc_di' or 'anoncreds'"
    assert "format" in errors.get("loc")
    assert errors.get("type") == "enum"


def test_invalid_credential_type_schema_invalid_verification_methods():
    """Test invalid CredentialType schema invalid verification_methods"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": "invalid",
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid list"
    assert "verification_methods" in errors.get("loc")
    assert errors.get("type") == "list_type"


def test_invalid_credential_type_schema_invalid_oca_bundle():
    """Test invalid CredentialType schema invalid oca_bundle"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "oca_bundle": "invalid",
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid dictionary"
    assert "oca_bundle" in errors.get("loc")
    assert errors.get("type") == "dict_type"


def test_invalid_credential_type_schema_invalid_mappings():
    """Test invalid CredentialType schema invalid mappings"""

    data = {
        "format": CredentialFormatEnum.VC_DI,
        "type": "BCPetroleum&NaturalGasTitle",
        "version": "1.0",
        "verification_methods": ["did:key:for:issuer"],
        "topic": {
            "type": "registration.registries.ca",
            "source_id": {"path": "$.path.to.topic.source_id"},
        },
        "mappings": "invalid",
    }

    with pytest.raises(ValidationError) as exc_info:
        CredentialType(**data)

    errors = exc_info.value.errors()[0]

    assert errors.get("msg") == "Input should be a valid list"
    assert "mappings" in errors.get("loc")
    assert errors.get("type") == "list_type"
