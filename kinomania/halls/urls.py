from django.urls import path
from kinomania.halls.views import DisplayHallView, HallDetailsView, CreateHallView, EditHallView, DeleteHallView

urlpatterns = [
    path("", DisplayHallView.as_view(), name="hall index"),
    path("details/<int:pk>/<str:slug>/", HallDetailsView.as_view(), name="hall details"),
    path("edit/<int:pk>/<str:slug>/", EditHallView.as_view(), name="edit hall"),
    path("delete/<int:pk>/<str:slug>/", DeleteHallView.as_view(), name="delete hall"),
    path("create/", CreateHallView.as_view(), name="create hall"),
]