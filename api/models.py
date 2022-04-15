from django.db import models

class Profile(models.Model):
    Name = models.CharField(max_length=100)
    city = models.IntegerField()

