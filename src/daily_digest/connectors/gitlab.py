import httpx

def get_merge_requests(config):
    gitlab_url = config["gitlab_url"]
    token = config["gitlab_token"]

    params = {
        'state': 'opened',
        'scope': 'assigned_to_me'
    }
    headers = {"PRIVATE-TOKEN": token}
    response = httpx.get(gitlab_url + "/api/v4/merge_requests", params=params, headers=headers)
    return response.raise_for_status().json()
