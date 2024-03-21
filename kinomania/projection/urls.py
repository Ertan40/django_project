from django.urls import path
from kinomania.projection.views import DisplayProjectionView, DisplayProjectionByDayView, CreateProjectionView


urlpatterns = [
    path("", DisplayProjectionView.as_view(), name="projection index"),
    path("add/", CreateProjectionView.as_view(), name='add projection'),
    path("<str:day>/", DisplayProjectionByDayView.as_view(), name='projection day'),
]