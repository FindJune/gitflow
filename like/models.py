from django.db import models

# Create your models here.

class like(models.Model):
    uid = models.IntegerField()
    wid = models.IntegerField()

    created = models.DataTimeField()
