from . import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'userAuthentication'

urlpatterns = [
<<<<<<< HEAD

=======
	path('', views.userauthpage, name=  "userauthpage"),
	path('accounts/', include('django.contrib.auth.urls')),
>>>>>>> e058e2784e23a62453c11f3dd2c6529c11aae0ae
]
