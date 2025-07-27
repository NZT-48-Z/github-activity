from api_client import fetch_github_activity
from output_formatter import format_events

async def get_user_activity(username):
    events = await fetch_github_activity(username)
    return format_events(events)
