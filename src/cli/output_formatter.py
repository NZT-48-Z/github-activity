def format_events(events):
    result = []

    for event in events:
        event_type = event.get("type", "")
        repo = event.get("repo", {}).get("name", "unknown/repo")
        payload = event.get("payload", {})

        if event_type == "PushEvent":
            commit_count = len(payload.get("commits", []))
            result.append(f"- Pushed {commit_count} commits to {repo}")

        elif event_type == "IssuesEvent":
            action = payload.get("action", "did something with an issue")
            result.append(f"- {action.capitalize()} an issue in {repo}")

        elif event_type == "WatchEvent":
            result.append(f"- Starred {repo}")

        elif event_type == "ForkEvent":
            forked_to = payload.get("forkee", {}).get("full_name", "another repo")
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
