from django.urls import path
from kinomania.projection.views import DisplayProjectionView, DisplayProjectionByDayView


urlpatterns = [
    path("", DisplayProjectionView.as_view(), name="projection index"),
    path("<str:day>/", DisplayProjectionByDayView.as_view(), name='projection day'),
]