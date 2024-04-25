from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views
from django.urls import reverse_lazy
from kinomania.reservation.models import Reservation
# Create your views here.

def index_reservation(request):
    return HttpResponse("reservation index")


class DisplayReservationView(views.ListView):
    model = Reservation
    template_name = "reservations/display-reservation-page.html"
