from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from social_django.models import UserSocialAuth

# To make a view require login for access, attach @login_required above it

@login_required
def homepage(request):
	return render(request, 'homepage/homepage.html')

@login_required
def logout(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    return render(request, 'userauth/logoutSuccess.html', {
        'github_login': github_login,
    })
