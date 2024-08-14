# Django specific settings
from datetime import date
from crud.models import *
from django.core.wsgi import get_wsgi_application
from django.db import connection
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
application = get_wsgi_application()


# Your code starts from here:
