from aiohttp import ClientSession

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "github-activity-cli",
}


async def get_github_activity(url):
    async with ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 404:
                return {"error": "User not found"}
            else:
                return {"error": response.status}
