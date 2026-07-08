from unittest.mock import patch, MagicMock

import httpx
import pytest

from daily_digest.connectors.redmine import (
    get_issues,
)
from daily_digest.enum import RedmineIssueRequest


@patch('daily_digest.connectors.redmine.httpx.get')
def test_get_assigned_issues_success(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = {
        'issues': [{'id': 1, 'project': {'id': 1, 'name': 'Project 1'}}]
    }

    mock_get.return_value = mock_response
    result = get_issues(config_fixture, RedmineIssueRequest.ASSIGNED)
    assert result == [{'id': 1, 'project': {'id': 1, 'name': 'Project 1'}}]


@patch('daily_digest.connectors.redmine.httpx.get')
def test_get_assigned_issues_failure(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )

    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_issues(config_fixture, RedmineIssueRequest.ASSIGNED)


@patch('daily_digest.connectors.redmine.httpx.get')
def test_get_expired_issues_success(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = mock_response
    mock_response.json.return_value = {
        'issues': [{'id': 1, 'project': {'id': 1, 'name': 'Project 1'}}]
    }

    mock_get.return_value = mock_response
    result = get_issues(config_fixture, RedmineIssueRequest.EXPIRED)
    assert result == [{'id': 1, 'project': {'id': 1, 'name': 'Project 1'}}]


@patch('daily_digest.connectors.redmine.httpx.get')
def test_get_expired_issues_failure(mock_get, config_fixture):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        message='HTTP 500', request=mock_get, response=mock_response
    )

    mock_get.return_value = mock_response
    with pytest.raises(httpx.HTTPStatusError, match='HTTP 500'):
        get_issues(config_fixture, RedmineIssueRequest.EXPIRED)
