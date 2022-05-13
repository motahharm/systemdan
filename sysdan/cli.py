"""This module contains the CLI for the sysdan package."""
# sysdan/cli.py

from typing import Optional
import typer
from sysdan import __app_name__, __version__

import platform
import os

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the current version",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command(name='os')
def os_info(vars: bool = False,
get_var: str = None) -> None:
    """Show the current operating system."""

    if get_var != None:
        value = os.getenv(get_var)
        if value != None:
            typer.echo(value)
        else:
            typer.echo(typer.style('No Variable Found', fg='red'))
        raise typer.Exit()

    os_name = platform.system()
    os_version = platform.release()
    os_arch = platform.machine()
    typer.echo(f"OS: {os_name}\nrelease: {os_version}\narchitecture: {os_arch}")

    if vars:
        env_vars = os.environ.items()
        if len(env_vars) == 0:
            typer.echo("No environment variables set")
            return
        typer.echo("\nEnvironment variables:")
        for key, value in env_vars:
            typer.echo(f"{key}: {value}\n")
