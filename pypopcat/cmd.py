import concurrent.futures
import os

import click

from pypopcat.constants import HOST, RATE_LIMIT
from pypopcat.emit import emit_clicks


@click.group()
def cli():
    '''pypopcat command line interface
    '''


@click.command()
@click.option('--limit',
              type=int,
              help="total number of clicks, None is infinite loop.")
@click.option('--country', default='TW', help='country code')
@click.option('--n_threads', default=1, type=int, help="number of windows")
@click.option('--proxy_server', default=None, type=str)
def emit(limit, country, n_threads, proxy_server):
    '''emit clicks on popcat.click
    '''
    with concurrent.futures.ThreadPoolExecutor(
            max_workers=n_threads) as executor:
        futures = {
            executor.submit(
                emit_clicks,
                HOST,
                RATE_LIMIT,
                limit,
                country,
                worker_id=i,
                proxy_server=proxy_server,
            )
            for i in range(n_threads)
        }


cli.add_command(emit)
