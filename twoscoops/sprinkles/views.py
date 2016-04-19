from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Sprinkle
from.decorators import check_sprinkles


def sprinkle_list(request):
    """Standard list view"""

    return render(request,  "sprinkles/sprinkle_list.html", {"sprinkles": Sprinkle.objects.all()})


def sprinkle_detail(request, pk):
    """Standard detail view"""
    sprinkle = get_object_or_404(Sprinkle, pk=pk)

    return render(request, "sprinkles/sprinkle_detail.html", {"sprinkle": sprinkle})