from django.db import models # type: ignore

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class Product(models.Model):
    pass