from django.db import models


class Sprinkle(models.Model):
    name = models.TextField(max_length=50)
    body = models.TextField(max_length=256)