"""This module contains the CLI for the systemdan package."""
# systemdan/cli.py

from typing import Optional
import typer
from systemdan import __app_name__, __version__
from systemdan import system_info

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

@app.command(name='info', help='Show system information')
def info() -> None:
    typer.echo(typer.style(f'\nSystem\n', fg=typer.colors.BLUE))
    sys_info = system_info.get_all_info()
    typer.echo(f'System: {sys_info["system"]}')
    typer.echo(f'Node: {sys_info["node"]}')
    typer.echo(f'Release: {sys_info["release"]}')
    typer.echo(f'Version: {sys_info["version"]}')
    typer.echo(f'Machine: {sys_info["machine"]}')
    typer.echo(f'Boot time: {sys_info["boot_time"]}')

    typer.echo(typer.style(f'\nCPU\n', fg=typer.colors.BLUE))
    cpu_info = system_info.get_cpu_info()
    typer.echo(f'Processor: {sys_info["processor"]}')
    typer.echo(f'Physical cores: {cpu_info["physical_cores"]}')
    typer.echo(f'Total cores: {cpu_info["total_cores"]}')
    typer.echo(f'Current frequency: {cpu_info["current_freq"]}')
    typer.echo(f'Min frequency: {cpu_info["min_freq"]}')
    typer.echo(f'Max frequency: {cpu_info["max_freq"]}')
    typer.echo(f'CPU list: {cpu_info["cpu_list"]}')
    typer.echo(f'CPU percent: {cpu_info["cpu_percent"]}')


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
