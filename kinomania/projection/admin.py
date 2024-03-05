from django.contrib import admin
from kinomania.projection.models import Projection

# Register your models here.
@admin.register(Projection)
class ProjectionAdmin(admin.ModelAdmin):
    ...