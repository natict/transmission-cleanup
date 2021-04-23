#!/usr/bin/env python3

import logging
import os

from transmission_rpc import Client

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST', '127.0.0.1')
PORT = int(os.environ.get('PORT', 9091))


def cleanup():
    c = Client(username=USERNAME, password=PASSWORD, host=HOST, port=PORT)

    ids_to_remove = [t.id for t in c.get_torrents() if t.date_done]

    if ids_to_remove:
        logging.info('Removing %s torrents...', len(ids_to_remove))
        c.remove_torrent(ids=ids_to_remove)
    else:
        logging.info('No torrents to remove')


if __name__ == '__main__':
    cleanup()
