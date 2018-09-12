import time
import logging

logger = logging.getLogger(__name__)


def basic_levels():
  logger.info('{:-^100}'.format(' BASIC LEVELS '))
  # Examples of logging API usage
  logger.debug('This is a simple DEBUG level message.')
  logger.info('This is a simple INFO level message.')
  logger.warning('This is a simple WARNING level message.')
  logger.warn('This is a simple WARN level message.')
  logger.error('This is a simple ERROR level message.')
  logger.exception('This is an ERROR level message with exc_info.')

  try:
    raise Exception('Random exception!')
  except Exception:
    logger.exception('This is an ERROR level message with a stack trace!')

  logger.critical('This is a simple CRITICAL level message')
  logger.fatal('This is a simple FATAL level message')

  # AND you can use the generic log method (but please don't).
  logger.log(logging.DEBUG, 'This is the same as logging.debug')
  logger.log(logging.INFO, 'This is the same as logging.info')
  logger.log(logging.WARNING, 'This is the same as logging.warning')
  logger.log(logging.WARN, 'This is the same as logging.warn')
  logger.log(logging.ERROR, 'This is the same as logging.exception', exc_info=True)
  logger.log(logging.CRITICAL, 'This is the same as logging.critical')
  logger.log(logging.FATAL, 'This is the same as logging.fatal')


def message_arguments():

    logger.info('{:-^100}'.format(' MESSAGE ARGUMENTS '))
    logger.info(
        'What %s is it? %.5f',
        'time', time.time()
    )

    logger.info(
        'Now with %(my_arg)s arguments!',
        {'my_arg': 'named'}
    )


def main():
    # Demo of basic log levels API
    basic_levels()

    # Demo of message formatting/calling convention
    message_arguments()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
