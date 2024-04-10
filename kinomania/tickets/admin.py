from django.contrib import admin
from kinomania.tickets.models import Ticket
# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["ticket_type", "price", "weekend_price"]