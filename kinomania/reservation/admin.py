from django.contrib import admin
from kinomania.reservation.models import Reservation
# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["date", "user", "projection", "is_finished"]
    list_filter = ["is_finished", "date"]
    ordering = ["date", "user"]