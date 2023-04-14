from django.db import models
from django.urls import reverse

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    birthday = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('student_update', kwargs={'pk': self.pk})