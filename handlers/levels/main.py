import logging


def make_handler(with_level=None):
    hdlr_level = with_level if with_level is not None else "no level"
    format_str = 'hdlr_level: {}'.format(hdlr_level)
    format_str += ' - %(levelname)s - %(message)s'
    formatter = logging.Formatter(format_str)

    # make a handler with a level
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    if with_level is not None:
        handler.setLevel(with_level)

    return handler


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # make a handler with a level
    handler_with_level = make_handler(with_level=logging.ERROR)

    # and without
    handler_without = make_handler()

    logger.addHandler(handler_with_level)
    logger.addHandler(handler_without)

    logger.info('My level my differ from my handler levels!')
    logger.error('This should have only been handled by one handler!')


if __name__ == '__main__':
    main()
