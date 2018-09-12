import logging


class MySpecialException(Exception):
    """We won't log this!"""


class SpecialExceptionFilter(logging.Filter):

    def filter(self, record):
        # Ask the question; "Should I log this?"

        if record.exc_info is not None:
            exc_type, value, tb = record.exc_info
            if exc_type is MySpecialException:
                return False

        return True


def main():
    exc_filter = SpecialExceptionFilter()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    logger.addFilter(exc_filter)

    logger.info('Hey, we have some special filters.')

    try:
        raise Exception()
    except Exception:
        logger.exception('This will be logged!')

    try:
        raise MySpecialException()
    except MySpecialException:
        logger.exception('This will not!!')


if __name__ == '__main__':
    main()
