import argparse
import struct
import logging
import socket
import json
import pickle


logger = logging.getLogger('server')


def serve(_socket):
    while True:
        conn, address = _socket.accept()
        # Shamelessly copied from logging.config
        chunk = conn.recv(4)
        slen = struct.unpack(">L", chunk)[0]
        chunk = conn.recv(slen)
        while len(chunk) < slen:
            chunk = chunk + conn.recv(slen - len(chunk))

        # Message is roughly JSON:
        try:
            message = json.loads(chunk)
        except ValueError:
            continue

        level = message['level']
        msg = message['msg']
        args = pickle.loads(message['args'])
        logger.log(level, msg, *args)


def run_server(host, port):
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.bind((host, port))
    _socket.listen(1)

    try:
        serve(_socket)
    except KeyboardInterrupt:
        _socket.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9999)
    parser.add_argument('--host', default='127.0.0.1')

    args = parser.parse_args()
    try:
        run_server(args.host, args.port)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
