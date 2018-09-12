import logging

import parent
from parent import first_child
from parent import second_child
from parent.first_child import grandchild

logger = logging.getLogger(__name__)


def main():
    logger.info('About to call package modules!')
    # call parent
    logger.info('Calling parent')
    parent.do_thing()

    # call first_child
    logger.info('Calling first child!')
    first_child.do_thing()

    # call second_child
    logger.info('Calling second child!')
    second_child.do_thing()

    # call grandchild
    logger.info('Calling grandchild!')
    grandchild.do_thing()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
