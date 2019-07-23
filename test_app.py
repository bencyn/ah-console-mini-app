from click.testing import CliRunner
from app import list

runner = CliRunner


def test_fetch_all_articles():
    result = runner.invoke(list)
    assert result.exit_code == 0
