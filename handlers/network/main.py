import argparse
import json
import logging
import pickle
import socket
import struct

logger = logging.getLogger(__name__)


class NetworkHandler(logging.Handler):

    def __init__(self, host, port, *args, **kwargs):
        super(NetworkHandler, self).__init__(*args, **kwargs)
        self.host = host
        self.port = port

    def emit(self, record):
        message = {
            'msg': record.msg,
            'level': record.levelno,
            'args': pickle.dumps(record.args or [])
        }
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _socket.connect((self.host, self.port))

        payload = json.dumps(message)
        _socket.send(struct.pack('>L', len(payload)))
        _socket.send(payload)
        _socket.close()


def poll_input():
    print('logging> Type a message (or level:message)!')
    while True:
        message = raw_input('logging> ')
        if message == 'q':
            break

        message_format = message.split(':', 1)
        if len(message_format) == 1:
            level = 'info'
            message = message_format[0]
        else:
            level = message_format[0].lower()
            message = message_format[1]

        if level.upper() not in logging._levelNames.keys():
            continue
        # Turn it into an int
        level = logging.getLevelName(level.upper())
        if not isinstance(level, int):
            level = logging.getLevelName(level)
        logger.log(level, message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9999)
    parser.add_argument('--host', default='127.0.0.1')
    args = parser.parse_args()

    handler = NetworkHandler(args.host, args.port)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    try:
        poll_input()
    except KeyboardInterrupt:
        print('Shutting down...')


if __name__ == '__main__':

    main()
