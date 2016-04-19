__author__ = 'plevytskyi'
from django.conf.urls import url
from flavor import views


urlpatterns = [
    url(regex=r"^$", view=views.FlavorCreateView.as_view(), name="flavor_create"),
    url(regex=r"^detail/(?P<slug>\w+)", view=views.FlavorDetailView.as_view(), name="detail")
    ]