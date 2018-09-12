import logging
from logging import config as logging_config


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - [%(module)s:%(levelname)s] - %(message)s"
        },
        "root": {
            "format": "ROOT - %(asctime)s - [%(module)s:%(levelname)s] - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default"
        },
        "root_console": {
            "class": "logging.StreamHandler",
            "formatter": "root"
        }
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": "INFO",
            # Don't send it up my namespace for additional handling
            "propagate": False
        }
    },
    "root": {
        "handlers": ["root_console"],
        "level": "INFO"
    }
}


def main():
    logging_config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.info('Hey, that was easy.')

    app_logger = logging.getLogger('app')
    app_logger.info('Hey, that was also easy.')


if __name__ == '__main__':
    main()
