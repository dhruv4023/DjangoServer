
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myserver.home import index
urlpatterns = [
    path('', index, name="home"),
    path('project/', include('myserver.Routes.project')),
    path('contact/', include('myserver.Routes.contact')),
    path('admin/', admin.site.urls),
]
