"""from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)

    duration = models.CharField(max_length=50)

    description = models.TextField()

    def __str__(self):
        return self.title


class Admission(models.Model):
    student_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    qualification = models.CharField(max_length=100)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


from django.db import models"""

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Admission(models.Model):

    # Link admission to the logged-in user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name