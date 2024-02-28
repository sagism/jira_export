import pytest
from config_loader import load_config
from unittest.mock import mock_open, patch

# Test loading valid configuration
def test_load_valid_config():
    mock_config = '{"instances": [{"url": "https://jira.example.com"}]}'
    with patch("builtins.open", mock_open(read_data=mock_config)):
        config = load_config("dummy_path.json")
        assert config["instances"][0]["url"] == "https://jira.example.com"

# Test handling of file not found
def test_load_config_file_not_found():
    with pytest.raises(Exception) as excinfo:
        load_config("nonexistent_file.json")
    assert "not found" in str(excinfo.value)

# Test handling of invalid JSON
def test_load_invalid_json():
    with patch("builtins.open", mock_open(read_data="not a valid json")):
        with pytest.raises(Exception) as excinfo:
            load_config("dummy_path.json")
        assert "not a valid JSON" in str(excinfo.value)

