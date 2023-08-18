from django.db import models

# Create your models here.
class Game(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField()
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    