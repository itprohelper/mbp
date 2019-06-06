import os
import json
from dotenv import load_dotenv
import pytest


from app import create_app
from app import db
# from app.models import (
#
# )

import config


basedir = os.path.join(os.path.dirname(__file__), '..')
load_dotenv(os.path.join(basedir, '.env'))
