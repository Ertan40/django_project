from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views
from kinomania.projection.models import Projection
# Create your views here.


def index_projection(request):
    return HttpResponse("projection index")


class DisplayProjectionView(views.ListView):
    model = Projection
    template_name = "projections/projection-main-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context