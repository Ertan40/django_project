from django import forms
from kinomania.tickets.models import Ticket


class TicketCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Ticket


class TicketEditForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Ticket


