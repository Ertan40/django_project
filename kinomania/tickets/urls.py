from django.urls import path
from kinomania.tickets.views import DisplayTicketView, CreateTicketView, EditTicketView, DeleteTicketView

urlpatterns = [
    path("", DisplayTicketView.as_view(), name="tickets index"),
    path("add/", CreateTicketView.as_view(), name="add ticket"),
    path("edit/<int:pk>/", EditTicketView.as_view(), name="edit ticket"),
    path("delete/<int:pk>/", DeleteTicketView.as_view(), name="delete ticket"),
]

