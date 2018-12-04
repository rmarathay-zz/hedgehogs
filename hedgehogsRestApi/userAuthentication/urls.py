from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'userAuthentication'

urlpatterns = [
	path('', views.userauthpage, name=  "userauthpage"),
	path('accounts/', include('django.contrib.auth.urls')),
]
