from django.db import models


class Activity(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
