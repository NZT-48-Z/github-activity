import pathlib
import click
import json

from cli.output_formatter import ColorOutput


CONFIG_PATH = pathlib.Path(__file__).resolve(
).parents[2].joinpath("config.json")


def check_config_exists():
    return CONFIG_PATH.exists()


def recreate_config():
    delete_config()
    create_config_interactive()


def delete_config():
    if CONFIG_PATH.exists():
        CONFIG_PATH.unlink()


def get_default_config():
    return {
        "token": "",
        "limit": 50,
        "sort_order": "desc",
        "show_time": True,
        "event_types": [
            "PushEvent",
            "IssuesEvent",
            "PullRequestEvent",
            "WatchEvent",
            "ForkEvent",
            "CreateEvent"
        ]
    }


def create_config(params: dict | None = None) -> None:
    if not CONFIG_PATH.exists():
        config_data = params if params else get_default_config()
        with open(CONFIG_PATH, "w", encoding="utf-8") as config_file:
            json.dump(config_data, config_file, indent=4)
        print(ColorOutput.action(f'\n✓ Config file created at {CONFIG_PATH}'))
    else:
        print(f"Config file already exists at {CONFIG_PATH}")


def create_config_interactive():
    click.echo(ColorOutput.info(
        "[Wizard] Welcome to the configuration wizard.")
    )

    token = click.prompt(ColorOutput.question(
        " ➔ Enter your token (used to increase API limits). You can leave empty if you don't have one"),
        default="",
        show_default=False,
    )

    while True:
        limit = click.prompt(ColorOutput.question(
            " ➔ Set request limit (default 50)"), default=50, type=int)
        if limit > 0:
            break
        else:
            click.echo(ColorOutput.warning("Please enter a positive integer."))

    sort_options = {"1": "asc", "2": "desc"}

    click.echo(ColorOutput.question(" ➔ Choose sort order:"))
    click.echo(ColorOutput.question("1 - Ascending (oldest first)"))
    click.echo(ColorOutput.question("2 - Descending (newest first)"))

    while True:
        sort_choice = click.prompt(ColorOutput.question(
            "Enter (default 2)"), type=click.Choice(["1", "2"]), default=2
        )
        sort_order = sort_options[sort_choice]
        break

    show_time = click.confirm(ColorOutput.question(
        " ➔ Show time for each activity?"), default=True)

    all_event_types = [
        "PushEvent",
        "IssuesEvent",
        "PullRequestEvent",
        "WatchEvent",
        "ForkEvent",
        "CreateEvent",
    ]

    click.echo(ColorOutput.question(
        " ➔ Do you want to include all event types?"))
    include_all = click.confirm(ColorOutput.question(
        " ➔ Include all event types?"), default=True)

    if include_all:
        selected_types = all_event_types.copy()
    else:
        selected_types = []
        click.echo(ColorOutput.question(
            " ➔ Select which event types to include:"))
        for event_type in all_event_types:
            if click.confirm(ColorOutput.question(f"Include {event_type}?"), default=True):
                selected_types.append(event_type)

    click.echo(ColorOutput.info("\n[Summary]"))
    click.echo(ColorOutput.hidden(
        f"Token: {'[hidden]' if token else '[none]'}"))
    click.echo(ColorOutput.action(f"Sort order: {sort_order}"))
    click.echo(ColorOutput.action(
        f"Show time: {'Yes' if show_time else 'No'}"))
    click.echo(ColorOutput.action(
        f"Event types to show: {', '.join(selected_types) if selected_types else '[none selected]'}"))

    if click.confirm(ColorOutput.warning("Save this configuration?"), default=True):
        config = {
            "token": token,
            "limit": limit,
            "sort_order": sort_order,
            "show_time": show_time,
            "event_types": selected_types,
        }
        create_config(config)
        click.echo(ColorOutput.action("✓ Configuration saved!\n"))
    else:
        create_config(get_default_config())
        click.echo(ColorOutput.warning(
            "Configuration was not saved. Default settings will be used. You can run --setup later to customize."))


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
