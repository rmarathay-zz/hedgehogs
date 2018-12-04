from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'tools'

urlpatterns = [
	path('', views.toolspage, name=  "toolpage"),
	path('graph/', views.graph_search, name="graph"),
]
