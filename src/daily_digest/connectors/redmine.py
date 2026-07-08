import datetime

import httpx

from daily_digest.enum import RedmineIssueRequest
from daily_digest.models import Config

LIMIT = 5


def get_issues(config: Config, request: RedmineIssueRequest) -> list[dict]:
    """Get assigned issues from Redmine."""

    headers = {'X-Redmine-API-Key': config.redmine_api_key}

    response = httpx.get(
        f'{config.redmine_url}/issues.json',
        params=_build_params(request),
        headers=headers,
    )

    return response.raise_for_status().json()['issues']


def _build_params(request: RedmineIssueRequest) -> dict[str, str | int]:
    match request:
        case RedmineIssueRequest.ASSIGNED:
            return {
                'assigned_to_id': 'me',
                'sort': 'updated_on:desc,priority:desc',
                'limit': LIMIT,
            }
        case RedmineIssueRequest.EXPIRED:
            now = datetime.datetime.now()
            return {
                'assigned_to_id': 'me',
                'sort': 'updated_on:desc',
                'due_date': now.strftime('%Y-%m-%d'),
                'limit': LIMIT,
            }
        case _:
            raise ValueError(f'Invalid request: {request}')
