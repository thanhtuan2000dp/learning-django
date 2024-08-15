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
# 1. Find learners with last name Smith
learner_smith = Learner.objects.filter(first_name='Smith')
print('1. Find learners with last name Smith')
print(learner_smith)
# 2. Find two youngest learners (ordered by dob)
youngest_learners = Learner.objects.order_by('-dob')[0:2]
print('2. Find two youngest learners (ordered by dob)')
print(youngest_learners)
