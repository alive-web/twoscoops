from django.core.urlresolvers import reverse
from django.db import models

from core.models import TastyTitleAbstractModel

STATUS = (
    (0, "zero"),
    (1, "one")
)


class Flavor(TastyTitleAbstractModel):

    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(default=0, choices=STATUS)

    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})

