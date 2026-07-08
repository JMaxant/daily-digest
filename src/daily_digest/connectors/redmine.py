import datetime

import httpx

from daily_digest.models import Config

LIMIT = 5


def get_assigned_issues(config: Config) -> list[dict]:
    """Get assigned issues from Redmine."""
    params: dict[str, str | int] = {
        'assigned_to_id': 'me',
        'sort': 'updated_on:desc,priority:desc',
        'limit': LIMIT,
    }
    headers = {'X-Redmine-API-Key': config.redmine_api_key}

    response = httpx.get(
        f'{config.redmine_url}/issues.json',
        params=params,
        headers=headers,
    )

    return response.raise_for_status().json()['issues']


def get_expired_issues(config: Config) -> list[dict]:
    now = datetime.datetime.now()
    params: dict[str, str | int] = {
        'assigned_to_id': 'me',
        'sort': 'updated_on:desc',
        'due_date': now.strftime('%Y-%m-%d'),
        'limit': LIMIT,
    }

    headers = {'X-Redmine-API-Key': config.redmine_api_key}
    response = httpx.get(
        f'{config.redmine_url}/issues.json',
        params=params,
        headers=headers,
    )

    return response.raise_for_status().json()['issues']
