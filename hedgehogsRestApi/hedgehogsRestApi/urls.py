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
from django.contrib.auth.views import LoginView, LogoutView
from analytics import views as analyticViews
app_name = 'home'
urlpatterns = [
    # @todo implement oauth in the userAuthentication application
    # @todo figure out a way to delete the null user from the database
    # @todo map everything to the improved GUI

    path('', views.homepage, name="homepage"),
    path('about/', include('about.urls', namespace='about')),
    path('tools/', include('tools.urls', namespace='tools')),
    path('data/', include('analytics.urls')),
    path('oauth/', include('social_django.urls',
                           namespace='social'), name="oauth"),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='userauth/login.html'),
         name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
