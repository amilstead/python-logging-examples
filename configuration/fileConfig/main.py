import os
import logging
from logging import config as logging_config


here = os.path.abspath(os.path.dirname(__file__))
LOGGING_CONFIG = os.path.abspath(os.path.join(here, 'config.ini'))


def main():
    logging_config.fileConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info('Hey, that was easy.')

    app_logger = logging.getLogger('app')
    app_logger.info('Hey, that was also easy.')


if __name__ == '__main__':
    main()
