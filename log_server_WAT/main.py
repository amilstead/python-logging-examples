import logging
from logging import config as logging_config

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    app.logger.info('Index page hit.')
    app.logger.debug('Helpful debug output!')
    return 'Hello, World!'


if __name__ == '__main__':
    log_server = logging_config.listen()
    log_server.start()
    # Set the level to INFO by default.
    app.logger.setLevel(logging.INFO)
    try:
        app.run()
    finally:
        logging_config.stopListening()
        log_server.join()
