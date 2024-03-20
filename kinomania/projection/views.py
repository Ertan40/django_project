from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views
from kinomania.projection.models import Projection
from kinomania.projection.helpers import get_days, get_today_movies, get_seats
import datetime
# Create your views here.


def index_projection(request):
    return HttpResponse("projection index")


class DisplayProjectionView(views.ListView):
    model = Projection
    template_name = "projections/projection-main-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = get_days()[0]
        context["date"] = today
        context["days"] = get_days()
        context["current_day"] = get_today_movies(today)
        context["current_day_date"] = str(today)
        return context


class DisplayProjectionByDayView(views.ListView):
    model = Projection
    template_name = "projections/display-projection-by-day.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.datetime.strptime(self.kwargs['day'], "%Y-%m-%d").date()
        context['days'] = get_days()
        context['current_day'] = get_today_movies(self.kwargs['day'])
        context['current_day_date'] = self.kwargs['day']
        return context
