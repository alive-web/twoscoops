from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    . fields.
    updating ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tasting(TimeStampedModel):
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=256)