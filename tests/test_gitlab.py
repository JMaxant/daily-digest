from unittest.mock import patch, MagicMock
from daily_digest.connectors.gitlab import get_merge_requests, get_pipelines

import httpx
import pytest


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_merge_requests_success(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = [{'id': 1, 'title': 'My MR'}]

    mock_get.return_value = mock_response

    result = get_merge_requests(config_fixture)

    assert result == [{'id': 1, 'title': 'My MR'}]


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_merge_requests_failure(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )

    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_merge_requests(config_fixture)


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_pipelines(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = []
    mock_get.return_value = mock_response
    result = get_pipelines(config_fixture)

    assert result == {'12345': [], '67890': []}


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_pipelines_failure(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )
    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_pipelines(config_fixture)


@patch('daily_digest.connectors.gitlab.httpx.get')
def test_get_pipelines_failure_with_invalid_project_ids(
    mock_get, config_fixture
):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )
    mock_get.return_value = mock_response
    config_fixture.gitlab_project_ids = ['invalid_project_id']
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_pipelines(config_fixture)
