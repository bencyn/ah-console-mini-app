# cli.py
import click
import requests
import pprint
import json

base_url = "https://ah-premier-staging.herokuapp.com/api/"


def get(param):
    try:
        response = requests.get(base_url+param)
        response.raise_for_status()
        return response

    except Exception as error:
        click.secho(str(error), fg="red")


def format(data):
    pp = pprint.PrettyPrinter(indent=2)
    return pp.pprint(data)


@click.group()
def cli():
    print("==== Console AH Mini App =====")


@cli.command()
def list():
    url_format = "articles/"
    response = get(url_format)
    try:
        click.echo(format(response.json()['articles']))
    except Exception:
        click.secho("List article response error", fg="red")


@cli.command()
@click.argument("slug")
def view(slug):

    url_format = "articles/{}".format(slug)
    response = get(url_format)
    try:
        click.echo(format(response.json()['article']))
    except Exception:
        exit(1)


@cli.command()
@click.argument("slug")
def export(slug):
    url_format = 'articles/{}'.format(slug)

    response = get(url_format)
    try:
        data = response.json()
    except Exception:
        click.secho("response error", fg="red")

    try:
        with open('exports/articles/article.json', 'w') as outfile:
            json.dump(data, outfile)
        click.secho(
            "Article {} exported successfully ".format(slug), fg="green")
    except Exception as error:
        click.secho(str(error), fg="red")
