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

# 1. Find a single instructor with first name Yan
instructor_yan = Instructor.objects.get(first_name='Yan')
print('1. Find a single instructor with first name `Yan`')
print(instructor_yan)

print('\n')

# 2. Try to find a non-existing instructor with first name Andy
try:
    instructor_andy = Instructor.objects.get(first_name='Andy')
except:
    print('2. Try to find a non-existing instructor with first name Andy')
    print("Instructor Any doesn't exist")

print('\n')

# 3. Find all part time instructors
part_time_instructor = Instructor.objects.filter(full_time=False)
print('3. Find all part time instructors')
print(part_time_instructor)

print('\n')

# 4. Find all full time instructors with First Name starts with Y and learners count greater than 30000
full_time_instructor = Instructor.objects.exclude(full_time=False).filter(
    total_learners__gt=30000).filter(first_name__startswith='Y')
print('4. Find all full time instructors with First Name starts with Y and learners count greater than 30000')
print(full_time_instructor)

print('\n')

# 5. Find all full time instructors with First Name starts with Y and learners count greater than 30000 using multiple parameters
full_time_instructor = Instructor.objects.filter(
    full_time=True, total_learners__gt=30000, first_name__startswith='Y')
print('5. Find all full time instructors with First Name starts with Y and learners count greater than 30000 using multiple parameters')
print(full_time_instructor)
