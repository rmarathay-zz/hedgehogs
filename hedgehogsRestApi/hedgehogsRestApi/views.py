from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth
import os

BASE_DIR = os.path.realpath('.')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'userauth/signup.html', {'form': form})

@login_required
def homepage(request):
	return render(request, BASE_DIR+'/templates/homepage/homepage.html')

@login_required
def logout(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'userauth/logout.html', {
        'github_login': github_login,
        'can_disconnect': can_disconnect
    })
