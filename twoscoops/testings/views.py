from django.views.generic import DetailView, ListView, TemplateView, UpdateView
from django.core.urlresolvers import reverse

from .models import Tasting


class FreshFruitMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FreshFruitMixin, self).get_context_data(**kwargs)
        context["has_fresh_fruit"] = "Test"
        return context


class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = "fruity_flavor.html"


class TasteListView(ListView):
    model = Tasting


class TasteDetailView(DetailView):
    model = Tasting


class TasteResultsView(TasteDetailView):
    template_name = "tastings/results.html"


class TasteUpdateView(UpdateView):
    model = Tasting
    fields = ('name', 'body')

    def get_success_url(self):
        return reverse("tastings:detail", kwargs={"pk": self.object.pk})
