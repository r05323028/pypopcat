import click

from pypopcat.constants import RATE_LIMIT, HOST
from pypopcat.emit import emit_clicks


@click.group()
def cli():
    '''pypopcat command line interface
    '''

@click.command()
@click.option('--limit', type=int)
@click.option('--country', default='TW')
def emit(limit, country):
    '''emit clicks on popcat.click
    '''
    emit_clicks(HOST, RATE_LIMIT, limit, country)

cli.add_command(emit)
