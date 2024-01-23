from django.urls import path, include
from kinomania.common.views import IndexView, AdminIndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('adminstaff/', AdminIndexView.as_view(), name='admin index'),
]