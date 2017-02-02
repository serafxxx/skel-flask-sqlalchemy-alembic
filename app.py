import os
from logging import config as logging_config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
# Apply configuration
app.config.from_object(config)
# Setup logger
log = app.logger
logging_config.dictConfig(config.LOGGING)

db = SQLAlchemy(app, session_options={'autocommit': False, 'autoflush': False} )


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
