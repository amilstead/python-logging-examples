import argparse
import logging

logger = logging.getLogger(__name__)


def make_arg_parser():
    argument_parser = argparse.ArgumentParser()
    # Streams
    argument_parser.add_argument(
        '-s', '--stream',
        choices=['sys.stderr', 'sys.stdout'],
        default='sys.stderr'
    )
    # Levels
    level_names = [
        level
        for level in logging._levelNames.keys()
        if isinstance(level, str)
    ]
    argument_parser.add_argument(
        '-l', '--level',
        choices=sorted(level_names),
        default='INFO'
    )
    # Files
    argument_parser.add_argument('-f', '--filename')
    argument_parser.add_argument('-m', '--filemode')

    # Formats
    argument_parser.add_argument('-dfmt', '--datefmt')
    argument_parser.add_argument('-fmt', '--msgfmt')
    return argument_parser


def extract_config(parsed_args):
    config_options = {
        'level': logging.INFO
    }
    if parsed_args.level is not None:
        config_options['level'] = logging.getLevelName(parsed_args.level)

    if parsed_args.stream is not None:
        config_options['stream'] = eval(parsed_args.stream)

    if parsed_args.filename is not None:
        config_options['filename'] = parsed_args.filename
        if parsed_args.filemode is not None:
            config_options['filemode'] = parsed_args.filemode

    if parsed_args.msgfmt is not None:
        config_options['format'] = parsed_args.msgfmt

    if parsed_args.datefmt is not None:
        config_options['datefmt'] = parsed_args.datefmt

    return config_options


def main():
    logger.debug('I used .debug!')
    logger.info('I used .info!')
    logger.warn('I used .warn!')
    logger.error('I used .error!')
    try:
        raise Exception('Some crazy exception!')
    except Exception:
        logger.exception('I used .execption!')


if __name__ == '__main__':
    # For eval parsing.
    exec 'import sys'
    parser = make_arg_parser()
    logging.basicConfig(**extract_config(parser.parse_args()))
    main()
