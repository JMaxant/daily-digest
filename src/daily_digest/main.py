from daily_digest.config import get_config
from daily_digest.connectors.gitlab import get_merge_requests
from daily_digest.connectors.redmine import (
    get_assigned_issues,
    get_expired_issues,
)
from daily_digest.renderers.terminal import (
    render_merge_requests,
    render_assigned_issues,
    render_expired_issues,
)


def main():
    config = get_config()
    result = get_merge_requests(config)
    render_merge_requests(result)

    render_assigned_issues(get_assigned_issues(config))
    render_expired_issues(get_expired_issues(config))


if __name__ == '__main__':
    main()
