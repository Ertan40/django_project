from django import forms

from kinomania.movies.models import Movie


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"



class MovieEditForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"