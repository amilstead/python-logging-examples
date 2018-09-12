import io
import logging
import sys


def stderr_logger():
    logger = logging.getLogger('stderr_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream=sys.stderr)  # also the default
    logger.addHandler(handler)

    logger.info('This is through sys.stderr!')


def stdout_logger():
    logger = logging.getLogger('stdout_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(stream=sys.stdout)  # also the default
    logger.addHandler(handler)

    logger.info('This is through sys.stdout!')


def bytestream_logger():

    # A file "stream"
    logger = logging.getLogger('bytestream_logger')
    logger.setLevel(logging.INFO)
    with io.BytesIO() as _buffer:
        handler = logging.StreamHandler(stream=_buffer)
        logger.addHandler(handler)
        logger.info('This is being written to an I/O buffer!')
        print(_buffer.getvalue())


def main():
    stderr_logger()
    stdout_logger()
    bytestream_logger()


if __name__ == '__main__':
    main()
