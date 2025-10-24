# This file also should be ignored by .gitignore but this for learning goles so yeah

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sercret_string'