__author__ = 'plevytskyi'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r"^$",
        view=views.TasteListView.as_view(),
        name="list"
        ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.TasteDetailView.as_view(),
        name="detail"
        ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.TasteResultsView.as_view(),
        name="results"
        ),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.TasteUpdateView.as_view(),
        name="update"
    ),
    url(regex=r"^mix/$", view=views.FruityFlavorView.as_view(), name="mix"),
]