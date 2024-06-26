from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kinomania.common.urls')),
    path('accounts/', include('kinomania.accounts.urls')),
    path('movies/', include('kinomania.movies.urls')),
    path('halls/', include('kinomania.halls.urls')),
    path('projection/', include('kinomania.projection.urls')),
    path('tickets/', include('kinomania.tickets.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)