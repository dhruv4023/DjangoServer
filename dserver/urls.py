
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myserver.home import *
urlpatterns = [
    path('', index, name="home"),
    path('adminlogin/', adminLogin, name="admin"),
    path('project/', include('myserver.Routes.project')),
    path('contact/', include('myserver.Routes.contact')),
    path('chat/', include('myserver.Routes.chat')),
    path('mail/', include('myserver.Mail.routes')),
    # path('expense/', include('myserver.Routes.expense')),
    path('admin/', admin.site.urls),
]
