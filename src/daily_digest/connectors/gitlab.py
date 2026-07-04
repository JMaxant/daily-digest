import httpx
from daily_digest.enum import GitlabMergeRequestsStatus

def get_merge_requests(config, state= GitlabMergeRequestsStatus.OPENED) -> list[dict]:
    gitlab_url = config["gitlab_url"]
    token = config["gitlab_token"]

    params = {
        'state': state,
        'scope': 'assigned_to_me'
    }

    headers = {"PRIVATE-TOKEN": token}
    response = httpx.get(gitlab_url + "/api/v4/merge_requests", params=params, headers=headers)
    return response.raise_for_status().json()

def get_pipelines(config) -> dict[str, list[dict]]:
    gitlab_url = config["gitlab_url"]
    token = config["gitlab_token"]
    headers = {"PRIVATE-TOKEN": token}
    ids = config["gitlab_project_ids"]
    ids = ids.split(",")
    pipelines = {}
    for project_id in ids:
        response = httpx.get(f"{gitlab_url}/api/v4/projects/{project_id}/pipelines", headers=headers)
        pipelines[project_id] = response.raise_for_status().json()

    return pipelines