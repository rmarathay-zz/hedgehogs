from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'about'

urlpatterns = [
    path('', views.aboutpage, name="aboutpage"),
]
