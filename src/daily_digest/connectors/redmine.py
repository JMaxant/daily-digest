import httpx

from daily_digest.models import Config

LIMIT = 25


def get_assigned_issues(config: Config) -> list[dict]:
    """Get assigned issues from Redmine."""
    params = {'assigned_to_id': 'me', 'sort': 'updated_on:desc', 'limit': LIMIT}
    headers = {'X-Redmine-API-Key': config.redmine_api_key}

    response = httpx.get(
        f'{config.redmine_url}/issues.json',
        params=params,
        headers=headers,
    )

    return response.raise_for_status().json()['issues']
