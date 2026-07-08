from datetime import datetime


def render_merge_requests(merge_requests_data: list[dict]) -> None:
    for data in merge_requests_data:
        created_at = datetime.fromisoformat(data['created_at'])
        updated_at = datetime.fromisoformat(data['updated_at'])
        print(f'{data["title"]} — {data["references"]["full"]}')
        print(
            f'  {data["author"]["name"]} | {created_at.strftime("%d-%m-%Y, %H:%M")} | {updated_at.strftime("%d-%m-%Y, %H:%M")}'
        )
        print(f'  {data["source_branch"]} -> {data["target_branch"]}')
        print(f'  {data["web_url"]}')
        print('-' * 60)


def render_assigned_issues(issues: list[dict]) -> None:
    for data in issues:
        print(f'{data["project"]["name"]} - {data["subject"]} ')
        print(f'  {data["description"][:200]}')
        print('-' * 60)


def render_expired_issues(issues: list[dict]) -> None:
    for data in issues:
        print(f'{data["subject"]}')
        print(f'  {data["description"]}')
        print('-' * 60)
