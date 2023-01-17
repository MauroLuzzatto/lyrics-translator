import click.testing
import pytest

from lyrics_translator import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    result = runner.invoke(console.main, ["--testing", "True"])
    assert result.exit_code == 0
