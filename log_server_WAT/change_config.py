import argparse
import logging
import os
import socket
import struct
import sys
from logging import config as logging_config

logger = logging.getLogger(__name__)


def make_arg_parser():
    argument_parser = argparse.ArgumentParser()
    # Files
    argument_parser.add_argument('-f', '--filename')
    return argument_parser


def _send_payload(payload):

    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.connect(('localhost', logging_config.DEFAULT_LOGGING_CONFIG_PORT))
    try:
        _socket.send(struct.pack('>L', len(payload)))
        _socket.send(payload)
    except Exception:
        logger.exception('Failed to send dictConfig update!')
        raise


def main():
    parser = make_arg_parser()
    args = parser.parse_args()
    if args.filename is None:
        print('--filename is required!')
        sys.exit(parser.print_help())

    if not os.path.exists(args.filename):
        print("Path '{}' does not exist!".format(args.filename))
        sys.exit(parser.print_help())

    with open(args.filename) as _config:
        file_contents = _config.read()
    _send_payload(file_contents)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
