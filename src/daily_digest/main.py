from daily_digest.config import get_config
from daily_digest.connectors.gitlab import get_merge_requests, get_pipelines


def main():
    config = get_config()
    result = get_merge_requests(config)
    print(result)
    res = get_pipelines(config)
    print(res)


if __name__ == '__main__':
    main()
