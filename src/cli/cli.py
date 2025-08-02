import click
import asyncio

from service import get_user_activity
from config_manager import (
    check_config_exists,
    create_config_interactive,
    create_config,
    load_config,
    recreate_config,
)
from output_formatter import ColorOutput


@click.command()
@click.argument("username", required=False)
@click.option("--setup","-s", is_flag=True, help="Run configuration setup")
def cli(username: str | None, setup: bool) -> None:
    if setup:
        if check_config_exists():
            if click.confirm(
                ColorOutput.warning(
                    "Configuration already exists. Do you want to recreate it?"),
                default=False,
            ):
                recreate_config()
            else:
                click.echo(ColorOutput.error("Configuration setup cancelled."))
        else:
            create_config_interactive()

    if not username:
        if setup:
            return
        else:
            click.echo(ColorOutput.error(
                "Username is required unless using --setup only."))
            return

    if not check_config_exists():
        if click.confirm(ColorOutput.info("[INFO] Config not found. Create it?"), default=True):
            create_config_interactive()
        else:
            create_config()
            click.echo(
                ColorOutput.warning(
                    "Default config created. Run with --setup to customize it later."
                )
            )

    config = load_config()
    click.echo(ColorOutput.info(f"Fetching activity for {username}..."))
    activity = asyncio.run(get_user_activity(username, config))

    for line in activity:
        click.echo(line)


if __name__ == "__main__":
    cli()
