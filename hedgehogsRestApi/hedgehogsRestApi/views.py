import django.contrib.postgres.search
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from social_django.models import UserSocialAuth
from django.core import mail

@login_required
def homepage(request):
	return render(request, 'homepage/homepage.html')

@login_required
def logout(request):
	user = request.user
	print("I am trying!\n")
	try:
		github_login = user.social_auth.get(provider='github')
		connection = mail.get_connection()
		email = mail.EmailMessage(
		    'Welcome to Hedgehogs!',
		    'Dear User,\n\nWe are so glad that you have tried out out app!\n-Ranjit',
		    'kwank2@rpi.edu',
		    [user.email],
		    connection=connection,
		)
		email.send() 
		print(user.email)
	except UserSocialAuth.DoesNotExist:
		github_login = None

	return render(request, 'userauth/logoutSuccess.html', {
		'github_login': github_login,
	})



