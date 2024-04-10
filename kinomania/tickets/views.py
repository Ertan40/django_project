from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views
from kinomania.tickets.models import Ticket
from django.urls import reverse_lazy
from kinomania.tickets.forms import TicketCreateForm
# Create your views here.
def index_tickets(request):
    return HttpResponse("tickets index")


class DisplayTicketView(views.ListView):
    model = Ticket
    template_name = "tickets/display-ticket-page.html"


class CreateTicketView(views.CreateView):
    # permission_required = "ticket.add_projection"
    # login_url = "profile/login"
    template_name = "tickets/add-ticket.html"
    success_url = reverse_lazy("ticket index")
    form_class = TicketCreateForm