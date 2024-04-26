from django.urls import path
from kinomania.reservation.views import create_reservation, save_projection, \
    ReservationStepOneView, ReservationStepTwoView, ReservationDetailsView

urlpatterns = [
    path("start/", create_reservation, name="reservation start"),
    path("save/<int:pk>/", save_projection, name="projection save"),
    path("stepone/", ReservationStepOneView.as_view(), name="reservation step one"),
    path("steptwo/", ReservationStepTwoView.as_view(), name="reservation step two"),
    path("details/<int:pk>/", ReservationDetailsView.as_view(), name="reservation details"),
]