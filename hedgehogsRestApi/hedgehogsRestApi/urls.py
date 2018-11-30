"""hedgehogsRestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
<<<<<<< HEAD
from django.contrib.auth.views import LoginView, LogoutView
=======
from analytics import views as analyticViews
>>>>>>> e058e2784e23a62453c11f3dd2c6529c11aae0ae

app_name = 'home'
urlpatterns = [
<<<<<<< HEAD
    # @todo implement oauth in the userAuthentication application
    # @todo figure out a way to delete the null user from the database
    # @todo map everything to the improved GUI

    path('', views.homepage, name = "homepage" ),
    path('about/', include('about.urls', namespace='about')),
    path('tools/', include('tools.urls', namespace='tools')),

    path('login/', LoginView.as_view(template_name='userauth/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('loggedout/', LogoutView.as_view(template_name='userauth/logoutSuccess.html'), name='logout'),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
=======
    path('admin/', admin.site.urls),
    path('', views.homepage, name = "homepage"),
    path('data/', include('analytics.urls')),
    path('graph/', views.graph_search, name="graph"),
    path('about/', include('about.urls', namespace='about')),
    path('tools/', include('tools.urls', namespace='tools')),
    path('userauth/', include('userAuthentication.urls', namespace='userauth')),
>>>>>>> e058e2784e23a62453c11f3dd2c6529c11aae0ae
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)