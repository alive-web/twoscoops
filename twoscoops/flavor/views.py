from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView

from .models import Flavor


class FlavorActionMixin(object):
    fields = ('title', 'slug', 'scoops_remaining')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)


class FlavorCreateView(FlavorActionMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')
    success_msg = "Flavor created!"


class FlavorUpdateView(FlavorActionMixin, UpdateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')
    success_msg = "Flavor updated!"


class FlavorDetailView(DetailView):
    model = Flavor