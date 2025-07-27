import click
import asyncio

from service import get_user_activity


@click.command()
@click.argument("username", type=str, required=True)
def main(username) -> None:
    click.echo(f"Fetching activity for {username}...")
    activity = asyncio.run(get_user_activity(username))
    
    for line in activity:
        click.echo(line)


if __name__ == "__main__":
    main()
