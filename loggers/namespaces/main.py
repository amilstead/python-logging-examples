import logging

logger = logging.getLogger(__name__)


def main():
    # There are a couple of ways to get the root logger:
    root_logger = logging.getLogger()
    logging.root.info('This is the root logger!')
    logging.info('This is also the root logger!')
    # Just to be safe!
    assert root_logger is logging.root

    # This is a logger with __main__, since that's what __name__ was.
    logger.info('This is the __main__ logger!')

    # Explicitly named loggers.
    named_logger = logging.getLogger('parent')
    named_logger.info('This is a named logger.')

    # Child loggers can come from `logger.getChild`
    child_logger = named_logger.getChild('first_child')
    child_logger.info('This is a child logger in the `foo.` namespace.')

    # Or by using dot-delimited strings in `logging.getLogger`
    other_child_logger = logging.getLogger('parent.first_child')
    other_child_logger.info('This is still a child in the `foo.` namespace.')
    assert child_logger is other_child_logger


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
