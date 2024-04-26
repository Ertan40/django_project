from django import forms
from kinomania.reservation.models import Reservation


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("projection",)
        exclude = "__all__"