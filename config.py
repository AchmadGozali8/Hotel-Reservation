"""configuration"""

import os
DEBUG = True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))
SQLALCHEMY_DATABASE_URI="mysql://root:ichal@localhost/reservation"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '8a0d87868f004541a99c6f6bddf4f9d5'