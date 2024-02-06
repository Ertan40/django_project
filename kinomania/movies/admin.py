from django.contrib import admin
from kinomania.movies.models import Movie
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "is_active"]
    list_filter = ["year", "is_active"]