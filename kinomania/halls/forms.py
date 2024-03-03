from django import forms

from kinomania.halls.models import Halls



class HallCreateForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'rows', 'seats_per_row', 'description', 'image')
        model = Halls



