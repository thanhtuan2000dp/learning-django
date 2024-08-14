from django.db import models
from django.utils.timezone import now

# Define your models from here:


class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self) -> str:
        return "First name: " + self.first_name+', ' + 'Last name: ' + self.last_name+', ' + 'Is full time:' + str(self.full_time) + ', ' + 'Total Learners: ' + str(self.total_learners)


class Course(models.Model):
    name = models.CharField(null=False, max_length=30,
                            default='onlince course')
    description = models.CharField(max_length=500)

    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)

    # Create a toString method for object string representation
    def __str__(self) -> str:
        return 'Name: ' + self.name + ', ' + 'Description:' + self.description
