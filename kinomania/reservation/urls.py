from django.urls import path
from kinomania.reservation.views import DisplayReservationView

urlpatterns = [
    path("", DisplayReservationView.as_view(), name="reservation index"),
]