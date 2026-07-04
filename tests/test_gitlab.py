from unittest.mock import patch, MagicMock
from daily_digest.connectors.gitlab import get_merge_requests, get_pipelines

import httpx
import pytest

from daily_digest.models import Config


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_merge_requests_success(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = [{'id': 1, 'title': 'My MR'}]

    mock_get.return_value = mock_response

    config = Config(
        gitlab_url='https://gitlab.example.com',
        gitlab_token='your_gitlab_token',
        gitlab_project_ids=[],
    )

    result = get_merge_requests(config)

    assert result == [{'id': 1, 'title': 'My MR'}]


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_merge_requests_failure(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500
    config = Config(
        gitlab_url='https://gitlab.example.com',
        gitlab_token='your_gitlab_token',
        gitlab_project_ids=[],
    )
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )

    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_merge_requests(config)


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_pipelines(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = []
    config = Config(
        gitlab_url='https://gitlab.example.com',
        gitlab_token='your_gitlab_token',
        gitlab_project_ids=['12345', '67890'],
    )
    mock_get.return_value = mock_response
    result = get_pipelines(config)

    assert result == {'12345': [], '67890': []}


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_pipelines_failure(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )
    config = Config(
        gitlab_url='https://gitlab.example.com',
        gitlab_token='your_gitlab_token',
        gitlab_project_ids=['12345', '67890'],
    )
    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_pipelines(config)
