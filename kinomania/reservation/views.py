import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from kinomania.reservation.models import Reservation
from kinomania.projection.models import Projection, Seat
from kinomania.projection.helpers import get_seats
from kinomania.reservation.forms import ReservationCreateForm
# Create your views here.

def save_projection(request, pk):
    request.session["projection_pk"] = str(pk)
    return redirect("reservation start")

@login_required
def create_reservation(request):
    projection_pk = int(request.session["projection_pk"])
    projection = Projection.objects.filter(pk=projection_pk).get()
    if request.method == "GET":
        form = ReservationCreateForm()
    else:
        today = str(datetime.datetime.today().date())
        reservation = Reservation(projection=projection, date=today, user=request.user)
        reservation.save()
        request.session["projection_pk"] = reservation.pk
        return redirect("reservation step one")

    context = {"form": form, "projection": projection, "seats": get_seats(projection),
               "free_seats": Seat.objects.filter(projection_id=projection_pk, is_taken=0).count()}

    return render(request, "reservations/reservation-start-page.html", context)


class ReservationStepOneView(LoginRequiredMixin, views.UpdateView):
    login_url = "/profile/login/"
    model = Reservation
    template_name = "reservations/reservation-step-one.html"
    fields = ("type_of_tickets", "number_of_tickets", "total_price")

    def get_object(self, queryset=None):
        reservation_pk = int(self.request.session.get("reservation_pk"))
        if reservation_pk:
            queryset = self.get_queryset()
            obj = queryset.filter(pk=reservation_pk).get()
            if obj:
                return obj

        raise Http404("No reservation found matching the query")



class ReservationStepTwoView(LoginRequiredMixin, views.UpdateView):
    login_url = "/profile/login/"
    model = Reservation
    template_name = "reservations/reservation-step-two.html"



class ReservationDetailsView(LoginRequiredMixin, views.DetailView):
    model = Reservation
    template_name = "reservations/reservation-details-page.html"
