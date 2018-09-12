import os
import logging

here = os.path.abspath(os.path.dirname(__file__))


def main():
    log_file = os.path.join(here, 'example.log')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.FileHandler(filename=log_file))

    logger.info('This goes to a file!')


if __name__ == '__main__':
    main()
