from django.urls import path
from kinomania.projection.views import DisplayProjectionView, DisplayProjectionByDayView, \
    CreateProjectionView, ProjectionDetailsView


urlpatterns = [
    path("", DisplayProjectionView.as_view(), name="projection index"),
    path("add/", CreateProjectionView.as_view(), name='add projection'),
    path("details/<int:pk>/", ProjectionDetailsView.as_view(), name='projection details'),
    # path("details/<int:pk>/<str:slug>/", ProjectionDetailsView.as_view(), name='projection details'),
    path("<str:day>/", DisplayProjectionByDayView.as_view(), name='projection day'),
]