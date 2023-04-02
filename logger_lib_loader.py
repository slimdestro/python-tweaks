from flask import Flask
import os
import logging
import rollbar
import logzio

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# reads rollbar/logzio keys from env. 
# it loads logzio/rollbar based on value set for ROLLBAR | LOGZIO
def __init__(self):
    switch = os.environ.get('ROLLBAR')
    if switch == 'active':
        rollbar.init(os.environ.get('ROLLBAR_ACCESS_TOKEN'), os.environ.get('ENVIRONMENT'))
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().addHandler(rollbar.logging.handlers.RollbarHandler())
    elif os.environ.get('LOGZIO') == 'active':
        logzio_handler = logzio.LogzioHandler(logzio_token=os.environ.get('LOGZIO_TOKEN'), logzio_type=os.environ.get('LOGZIO_TYPE'))
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().addHandler(logzio_handler)
    else:
        pass

@app.route('/')
def index():
    logger.info('This is an info message')
    return 'Hello World!'

if __name__ == '__main__':
    app.run()