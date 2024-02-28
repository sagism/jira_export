import pytest
from jira_connector import fetch_jira_items
from unittest.mock import patch, MagicMock

# Mock JIRA issue response
mock_issues = [
    MagicMock(fields=MagicMock(summary="Issue 1", description="Description 1", status="Open")),
    MagicMock(fields=MagicMock(summary="Issue 2", description="Description 2", status="Done")),
]

# Test fetching issues with mocked JIRA client
@patch('jira_connector.JIRA')
def test_fetch_jira_items(mock_jira):
    mock_jira.return_value.search_issues.return_value = mock_issues
    instance_config = {
        "url": "https://jira.example.com",
        "username": "test",
        "password": "test",
        "query": "project = TEST",
        "field_mapping": {
            "summary": "Title",
            "description": "Details",
            "status": "Current Status"
        },
        "value_mapping": {
            "status": {
                "Open": "Pending",
                "Done": "Completed"
            }
        }
    }
    issues = fetch_jira_items(instance_config)
    assert len(issues) == 2
    assert issues[0]["Title"] == "Issue 1"
    assert issues[0]["Current Status"] == "Pending"
    assert issues[1]["Title"] == "Issue 2"
    assert issues[1]["Current Status"] == "Completed"

# Here you can add more tests, for example, testing error handling, or testing with different configurations

