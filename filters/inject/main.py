import logging


class MySpecialException(Exception):
    """We won't log this!"""
    def __init__(self, special_value):
        self.special_value = special_value


class SpecialExceptionFilter(logging.Filter):

    def filter(self, record):
        # Ask the question; "Should I log this?"
        record.special_exc_value = None
        if record.exc_info is not None:
            exc_type, value, tb = record.exc_info
            if exc_type is MySpecialException:
                record.special_exc_value = value.special_value

        return True


def main():
    exc_filter = SpecialExceptionFilter([MySpecialException])
    formatter = logging.Formatter(
        '%(levelname)s - %(special_exc_value)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Add the filter, so we have context.
    logger.addFilter(exc_filter)

    # Then add a handler/formatter who knows how to process it.
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('Hey, we have some special filters.')

    try:
        raise MySpecialException('special_context')
    except MySpecialException:
        logger.exception('This message has special format data!')


if __name__ == '__main__':
    main()
