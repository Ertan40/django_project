from django.urls import path
from kinomania.projection.views import DisplayProjectionView


urlpatterns = [
    path("", DisplayProjectionView.as_view(), name="projection index"),
]