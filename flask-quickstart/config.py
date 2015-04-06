# coding=utf8

import os
from datetime import datetime

META = {
    'author': os.environ.get('FLASK_AUTHOR'),
    'github': os.environ.get('FLASK_AUTHOR_GITHUB'),
    'datetime': str(datetime.now())
}
