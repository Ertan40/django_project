from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views
from kinomania.projection.models import Projection, Seat
from kinomania.projection.helpers import get_days, get_today_movies, get_seats
import datetime
from django.urls import reverse_lazy
from kinomania.projection.forms import ProjectionCreateForm
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



class CreateProjectionView(views.CreateView):
    permission_required = "projection.add_projection"
    login_url = "profile/login"
    template_name = "projections/add-projection.html"
    success_url = reverse_lazy("projection index")
    form_class = ProjectionCreateForm



class ProjectionDetailsView(views.DetailView):
    model = Projection
    template_name = "projections/projection-details-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seats"] = get_seats(self.object)
        context["free_seats"] = Seat.objects.filter(projection_id=self.object.id, is_taken=0).count()
        return context



