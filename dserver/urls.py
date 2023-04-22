
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myserver.controller import index
urlpatterns = [
    path('', index, name="home"),
    path(settings.SERVER_URL+'project/', include('myserver.projectUrls')),
    path('admin/', admin.site.urls),
]
