from unittest.mock import patch, MagicMock


from daily_digest.connectors.redmine import get_assigned_issues


@patch('daily_digest.connectors.redmine.httpx.get')
def test_get_assigned_issues_success(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = {
        'issues': [{'id': 1, 'project': {'id': 1, 'name': 'Project 1'}}]
    }

    mock_get.return_value = mock_response
    result = get_assigned_issues(config_fixture)
    assert result == [{'id': 1, 'project': {'id': 1, 'name': 'Project 1'}}]
