import httpx
from daily_digest.enum import GitlabMergeRequestsStatus
from daily_digest.models import Config


def get_merge_requests(
    config: Config, state=GitlabMergeRequestsStatus.OPENED
) -> list[dict]:
    params = {'state': state.value, 'scope': 'assigned_to_me'}

    headers = {'PRIVATE-TOKEN': config.gitlab_token}
    response = httpx.get(
        config.gitlab_url + '/api/v4/merge_requests',
        params=params,
        headers=headers,
    )

    return response.raise_for_status().json()


def get_pipelines(config: Config) -> dict[str, list[dict]]:
    headers = {'PRIVATE-TOKEN': config.gitlab_token}
    ids = config.gitlab_project_ids
    pipelines = {}
    for project_id in ids:
        response = httpx.get(
            f'{config.gitlab_url}/api/v4/projects/{project_id}/pipelines',
            headers=headers,
        )
        pipelines[project_id] = response.raise_for_status().json()

    return pipelines
