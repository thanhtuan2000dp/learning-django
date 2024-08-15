# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection  # noqa: E402
# Ensure settings are read
from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()

from related_objects.models import *  # noqa: E402
from datetime import date  # noqa: E402


# Your code starts from here:
# 1. Get courses taught by Instructor Yan, via both forward (explicit) and backward (implicit) access
courses = Course.objects.filter(instructors__first_name='Yan')
print('1. Get courses taught by Instructor Yan, forward')
print(courses)

print('\n')

instructor_yan = Instructor.objects.get(first_name='Yan')
print('1. Get courses taught by Instructor Yan, backward')
print(instructor_yan.course_set.all())

print('\n')

# 2. Get the instructors of Cloud app dev course
instructors = Instructor.objects.filter(course__name__contains='Cloud')
print('2. Get the instructors of Cloud app dev course')
print(instructors)
print('\n')

# 3. Check the occupations of the courses taught by instructor Yan
courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print('3. Check the occupations of the courses taught by instructor Yan')
print(occupation_list)
