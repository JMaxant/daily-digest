import pytest

from daily_digest.models import Config


@pytest.fixture
def dot_env_fixture() -> dict:
    return {
        'GITLAB_URL': 'https://gitlab.example.com',
        'GITLAB_TOKEN': 'fake-token',
        'GITLAB_PROJECT_IDS': '12345',
        'REDMINE_URL': 'https://redmine.example.com',
        'REDMINE_API_KEY': 'redmine-api-key',
    }


@pytest.fixture
def config_fixture() -> Config:
    return Config(
        gitlab_url='https://gitlab.example.com',
        gitlab_token='fake-token',
        gitlab_project_ids=['12345', '67890'],
        redmine_url='https://redmine.example.com',
        redmine_api_key='redmine-api-key',
    )
