from cli.api_client import fetch_github_activity
from cli.output_formatter import format_events, ColorOutput
from cli.config_manager import load_config


async def get_user_activity(username, config):
    if config is None:
        config = load_config()

    events = await fetch_github_activity(
        username, token=config.get("token", ""), limit=config.get("limit", "")
    )

    if isinstance(events, dict) and "error" in events:
        code = events["error"]
        if code == 403:
            return [
                f"❌ {ColorOutput.error('Error 403')}: Rate limit exceeded or forbidden (maybe token invalid)"
            ]
        elif code == 404:
            return [f"❌ {ColorOutput.error('Error 404')}: User '{username}' not found"]
        else:
            return [f"❌ {ColorOutput.error('Unexpected error')}: {code}"]

    if not isinstance(events, list):
        return [ColorOutput.error("❌ Unexpected response format from GitHub")]

    return format_events(
        events,
        show_time=config.get("show_time", True),
        event_types=config.get("event_types", []),
    )
