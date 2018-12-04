import django.contrib.postgres.search
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from hedgehogsRestApi.forms import SignUpForm
from social_django.models import UserSocialAuth
from django.core import mail
import sys

@login_required
def homepage(request):
	return render(request, 'homepage/homepage.html')

@login_required
def logout_view(request):
	user = request.user
	print("I am trying!\n")
	try:
		github_login = user.social_auth.get(provider='github')
	except UserSocialAuth.DoesNotExist:
		github_login = None
		logout(request)

	return render(request, 'userauth/logout.html', {
	'github_login': github_login,
	})

def signup_view(request):
	user = request.user
	if request.method == 'POST':
		form = SignUpForm(request.POST)
	
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)

			connection = mail.get_connection()
			message = ""

			file = open(sys.path[0]+'/hedgehogsRestApi/HedgehogsWelcomeEmail.txt',"r")
			for line in file:
				message += line + "\n"

			print(message)

			email = mail.EmailMessage(
				"Welcome to Hedgehogs!",
				message,
				'hedgehogsrcos@gmail.com',
				[user.email],
			)

			connection=connection
			email.send() 
			return redirect('homepage')
	else:
		form = SignUpForm()
	return render(request, 'userauth/signup.html', {'form': form})
