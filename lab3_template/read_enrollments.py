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
# 1. Get the user information about learner David
print('1. Get the user information about learner David')
learner_david = Learner.objects.get(first_name='David')
print(learner_david.user_ptr)

print('\n')

# 2. Get learner David information from user
print('2. Get learner David information from user')
user_david = User.objects.get(first_name='David')
print(user_david.learner)

print('\n')

# 3. Get all learners for Introduction to Python course
print('3. Get all learners for Introduction to Python course')
course = Course.objects.get(name='Introduction to Python')
learners = course.learners.all()
print(learners)
print('\n')

# 4. Check the occupation list for the courses taught by instructor Yan
print('4. Check the occupation list for the courses taught by instructor Yan')
courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print(occupation_list)
print('\n')

# 5. Check which courses the developer learners are enrolled in Aug, 2020
print('5. Check which courses the developer learners are enrolled in Aug, 2020')
enrolments = Enrollment.objects.filter(
    date_enrolled__month=8, date_enrolled__year=2020, learner__occupation='developer')
course_for_developers = set()
for enrollment in enrolments:
    course_for_developers.add(enrollment.course.name)
print(course_for_developers)
