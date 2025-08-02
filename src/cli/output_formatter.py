from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class ColorOutput:
    @staticmethod
    def warning(message: str) -> str:
        """Возвращает сообщение в желтом цвете"""
        return f"{Fore.YELLOW}{message}{Style.RESET_ALL}"

    @staticmethod
    def error(message: str) -> str:
        """Возвращает сообщение в красном цвете"""
        return f"{Fore.RED}{message}{Style.RESET_ALL}"

    @staticmethod
    def info(message: str) -> str:
        """Возвращает сообщение в голубом цвете"""
        return f"{Fore.CYAN}{message}{Style.RESET_ALL}"

    @staticmethod
    def question(message: str) -> str:
        """Возвращает сообщение в синем цвете"""
        return f"{Fore.BLUE}{message}{Style.RESET_ALL}"

    @staticmethod
    def action(message: str) -> str:
        """Возвращает сообщение в зеленом цвете"""
        return f"{Fore.GREEN}{message}{Style.RESET_ALL}"

    @staticmethod
    def hidden(message: str) -> str:
        """Возвращает сообщение в сером цвете для скрытой информации"""
        return f"{Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}"


def format_events(events, show_time=True, event_types=None):
    result = []

    for event in events:
        event_type = event.get("type", "")

        if event_types and event_type not in event_types:
            continue

        repo = event.get("repo", {}).get("name", "unknown/repo")
        payload = event.get("payload", {})
        created_at = event.get("created_at", "")

        time_str = ""
        if show_time and created_at and event_type in ["PushEvent", "WatchEvent"]:
            dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            time_str = f" [{dt.strftime('%Y-%m-%d %H:%M')}]"

        if event_type == "PushEvent":
            commit_count = len(payload.get("commits", []))
            result.append(
                f"- Pushed {commit_count} commits to {repo}{time_str}")

        elif event_type == "IssuesEvent":
            action = payload.get("action", "did something with an issue")
            result.append(f"- {action.capitalize()} an issue in {repo}")

        elif event_type == "WatchEvent":
            result.append(f"- Starred {repo}{time_str}")

        elif event_type == "ForkEvent":
            forked_to = payload.get("forkee", {}).get(
                "full_name", "another repo")
            result.append(f"- Forked {repo} to {forked_to}")

        elif event_type == "PullRequestEvent":
            action = payload.get("action", "interacted with pull request")
            result.append(f"- {action.capitalize()} a pull request in {repo}")

        elif event_type == "CreateEvent":
            ref_type = payload.get("ref_type")
            ref = payload.get("ref", repo)
            if ref_type == "repository":
                result.append(f"- Created repository {repo}")
            else:
                result.append(f"- Created {ref_type} '{ref}' in {repo}")

        else:
            result.append(f"- Did {event_type} in {repo}")

    return result
