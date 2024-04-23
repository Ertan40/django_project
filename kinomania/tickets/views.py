from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views
from kinomania.tickets.models import Ticket
from django.urls import reverse_lazy
from kinomania.tickets.forms import TicketCreateForm, TicketEditForm
# Create your views here.
def index_tickets(request):
    return HttpResponse("tickets index")


class DisplayTicketView(views.ListView):
    model = Ticket
    template_name = "tickets/display-ticket-page.html"


class CreateTicketView(views.CreateView):
    # permission_required = "ticket.add_ticket"
    # login_url = "/profile/login/"
    template_name = "tickets/add-ticket.html"
    success_url = reverse_lazy("tickets index")
    form_class = TicketCreateForm


class EditTicketView(views.UpdateView):
    # permission_required = "ticket.add_ticket"
    # login_url = "/profile/login/"
    template_name = "tickets/edit-ticket.html"
    success_url = reverse_lazy("tickets index")
    model = Ticket
    fields = "__all__"


class DeleteTicketView(views.DeleteView):
    # permission_required = "ticket.delete_ticket"
    # login_url = "/profile/login/"
    template_name = "tickets/delete-ticket.html"
    success_url = reverse_lazy("tickets index")
    model = Ticket