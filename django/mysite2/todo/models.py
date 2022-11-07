from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=140)
    done = models.BooleanField()
