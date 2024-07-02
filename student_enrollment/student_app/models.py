from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    place = models.CharField(max_length=100)
    address = models.TextField()
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name
