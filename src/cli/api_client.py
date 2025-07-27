from http_client import get_github_activity


async def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    return await get_github_activity(url)
