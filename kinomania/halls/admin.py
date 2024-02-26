from django.contrib import admin
from kinomania.halls.models import Halls

# Register your models here.
@admin.register(Halls)
class HallAdmin(admin.ModelAdmin):
    list_display = ["name", "rows", "seats_per_row"]