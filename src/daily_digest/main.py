from daily_digest.config import get_config
from daily_digest.connectors.gitlab import get_merge_requests
from daily_digest.connectors.redmine import (
    get_issues,
)
from daily_digest.enum import RedmineIssueRequest
from daily_digest.renderers.terminal import (
    render_merge_requests,
    render_issues,
)


def main():
    config = get_config()
    result = get_merge_requests(config)
    render_merge_requests(result)

    render_issues(get_issues(config, RedmineIssueRequest.ASSIGNED))
    render_issues(get_issues(config, RedmineIssueRequest.EXPIRED))


if __name__ == '__main__':
    main()
