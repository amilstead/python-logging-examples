import logging


def main():

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logger.info('This will default to the ISO-8601 timestamp format.')

    formatter.datefmt = '%A %b %d, %Y'
    handler.setFormatter(formatter)
    logger.info('Check out my new date format!')


if __name__ == '__main__':
    main()
