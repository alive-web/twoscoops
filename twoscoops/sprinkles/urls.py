__author__ = 'plevytskyi'
from django.conf.urls import url
from sprinkles.views import sprinkle_list


urlpatterns = [
    url(regex=r"^$", view=sprinkle_list, name="sprinkle")
    ]