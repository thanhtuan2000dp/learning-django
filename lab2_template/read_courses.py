# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")  # noqa: E402
from django.db import connection  # noqa: E402
# Ensure settings are read
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()

from crud.models import *  # noqa: E402
from datetime import date  # noqa: E401


# Your code starts from here:

# Find all courses
courses = Course.objects.all()
print(courses)
