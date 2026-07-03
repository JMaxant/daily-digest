from unittest.mock import patch, MagicMock

import httpx
import pytest

from daily_digest.connectors.gitlab import get_merge_requests


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_merge_requests_success(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = [{"id": 1, "title": "My MR"}]

    mock_get.return_value = mock_response

    config = {
        'gitlab_url': 'https://gitlab.example.com',
        'gitlab_token': 'your_gitlab_token',
    }

    result = get_merge_requests(config)

    assert result == [{"id": 1, "title": "My MR"}]

@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_merge_requests_failure(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500
    config = {
        'gitlab_url': 'https://gitlab.example.com',
        'gitlab_token': 'your_gitlab_token',
    }
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(message='HTTP 500', request=mock_get, response=mock_response)

    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'): get_merge_requests(config)