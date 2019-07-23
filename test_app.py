from app import list, view, export, cli, search
from click.testing import CliRunner
from app import list

runner = CliRunner

runner = CliRunner()


def test_fetch_all_articles():
    result = runner.invoke(list)
    assert result.exit_code == 0


def test_get_single_article():
    result = runner.invoke(view, ["blog-post-2"])
    assert result.exit_code == 0


def test_success_export_article():
    result = runner.invoke(export, ["blog-post-2"])
    assert result.exit_code == 0


def test_failed_export_article():
    result = runner.invoke(export, ["blogggies-post-2"])
    assert result.exit_code == 0


def test_failed_get_article():
    result = runner.invoke(export, ["blogggies-post-2"])
    assert "Not Found" in result.output


def test_search_article():
    result = runner.invoke(search, ["good"])
    assert result.exit_code == 0


def test_failed_search_article():
    result = runner.invoke(search, ["goodwew"])
    assert result.exit_code == 0


def test_cli():
    result = runner.invoke(cli)
    assert result.exit_code == 0
