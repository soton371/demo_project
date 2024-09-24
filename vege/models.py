from django.db import models # type: ignore

# Create your models here.
class Recipe(models.Model):
    # id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    recipe_des = models.TextField(null=True)
    recipe_img = models.ImageField(upload_to='recipe')


