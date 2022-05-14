"""test the cli module"""
# tests/test_systemdan.py

from unittest import result
from typer.testing import CliRunner
from systemdan import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

def test_info():
    result = runner.invoke(cli.app, ["info"])
    assert result.exit_code == 0
    assert "System" in result.stdout
    assert "Node" in result.stdout
    assert "Release" in result.stdout
    assert "Version" in result.stdout
    assert "Machine" in result.stdout
    assert "Boot time" in result.stdout

    assert "CPU" in result.stdout
    assert "Processor" in result.stdout
    assert "Physical cores" in result.stdout
    assert "Total cores" in result.stdout
    assert "Current frequency" in result.stdout
    assert "Min frequency" in result.stdout
    assert "Max frequency" in result.stdout
    assert "CPU list" in result.stdout
    assert "CPU percent" in result.stdout

def test_os():
    result = runner.invoke(cli.app, ["os"])
    assert result.exit_code == 0
    assert "OS" in result.stdout
    assert "release" in result.stdout
    assert "architecture" in result.stdout
