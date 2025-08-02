from aiohttp import ClientSession

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "github-activity-cli",
}


async def get_github_activity(url, token="", limit=30):
    headers = HEADERS.copy()
    if token:
        headers["Authorization"] = f"token {token}"

    params = {"per_page": limit}

    async with ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 404:
                return {"error": 404}
            else:
                return {"error": response.status}
