
###################################################################
#
#   History
#
#   2019-07-03  Todd Valentic
#               Initial implementation
#
###################################################################

import os
import uuid
import socket
import datetime

from . import metadata 

class Config(object):

    HOST = socket.gethostname()
    VERSION = metadata.version
    PROJECT = metadata.project
    BRANCH = metadata.branch

    # Mail configuration

    MAIL_SERVER = 'localhost'
    MAIL_DEFAULT_SENDER = 'no-reply@localhost'

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    JWT_ALGORITHM = 'HS256'
    JWT_HEADER_TYPE = 'bearer'
    JWT_TOKEN_LOCATION = ['headers','json']

    TEMPLATES_AUTO_RELOAD = True

    STATIC_FOLDER = 'server/templates/static'

    FLATPAGES_EXTENSION = ['.rst']

    SQLALCHEMY_URI = f'postgresql://@'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml',
                          'text/javascript', 'application/json',
                          'application/javascript','application/x-javascript']

class Production(Config):

    DEBUG = False
    PREFIX = f'{Config.SQLALCHEMY_URI}/{Config.PROJECT}.{Config.BRANCH}'

    SQLALCHEMY_DATABASE_URI = f'{PREFIX}-prod'
    SQLALCHEMY_BINDS = {
        'users':    f'{PREFIX}-users-prod'
    }

class Development(Config):

    DEBUG = True
    PREFIX = f'{Config.SQLALCHEMY_URI}/{Config.PROJECT}.{Config.BRANCH}'

    SQLALCHEMY_DATABASE_URI = f'{PREFIX}-devel'
    SQLALCHEMY_BINDS = {
        'users':    f'{PREFIX}-users-devel'
    }


