import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TESTING = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(base_dir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

TIME_ZONE = 'Europe/Moscow'


LOGS_PATH = os.path.join(base_dir, 'logs')
if not os.path.isdir(LOGS_PATH):
    os.makedirs(LOGS_PATH)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s'
        },
        'simple_console': {
            'format': '%(levelname)s %(name)s: %(message)s'
        },
        'email': {
            'format': '%(message)s\n\n%(asctime)s %(levelname)s %(name)s'
        },
        'push_notification':{
            'format': '%(message)s\n%(levelname)s %(name)s'
        }
    },
    'handlers': {
        # 'null': {
        #     'level':'DEBUG',
        #     'class':'django.utils.log.NullHandler',
        # },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple_console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_PATH, 'app.log'),
            'maxBytes': 10000,
            'backupCount': 5,
            'formatter': 'simple'
        },

        # 'push_notification': {
        #     'level': 'INFO',
        #     'class': 'util.logging_handlers.PushoverHandler',
        #     'formatter': 'push_notification',
        #     'api_token': POPOVER_API_TOKEN,
        #     'user_key': POPOVER_USER_KEY
        # }
    },
    'loggers': {
        'app': {
            # 'handlers':['console', 'file', 'push_notification'],
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
