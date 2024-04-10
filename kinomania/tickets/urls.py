from django.urls import path
from kinomania.tickets.views import DisplayTicketView, CreateTicketView

urlpatterns = [
    path("", DisplayTicketView.as_view(), name="tickets index"),
    path("add/", CreateTicketView.as_view(), name="add ticket"),
]

