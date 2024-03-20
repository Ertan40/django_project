from django.contrib import admin
from kinomania.projection.models import Projection

# Register your models here.
@admin.register(Projection)
class ProjectionAdmin(admin.ModelAdmin):
    list_filter = ["movie", "date", "hall"]
    ordering = ["movie", "date", "hour", "hall"]
    list_display = ["movie", "date", "hall", "formatted_hour"]
    search_fields = ["movie__title", "hall__name"]

    def formatted_hour(self, obj):
        return obj.hour.strftime('%H:%M')

    formatted_hour.short_description = 'Hour'