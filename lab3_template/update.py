# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection  # noqa: E402
# Ensure settings are read
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()

# Your code starts from here:
