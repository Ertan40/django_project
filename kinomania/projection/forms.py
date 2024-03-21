from django import forms

from kinomania.projection.models import Projection


class ProjectionCreateForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Projection
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "placeholder": "dd-mm-yyyy"}),
            "hour": forms.TimeInput(attrs={
                "type": "time", "placeholder": "HH:MM", "input_type": "%H:%M", "step": "900"}),
        }