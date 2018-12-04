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
import sys

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
		message = ""
		file = open(sys.path[0]+'\\hedgehogsRestAPI\\HedgehogsWelcomeEmail.txt', "r")
		for line in file:
			message += line + "\n" 
		email = mail.EmailMessage(
		    'Welcome to Hedgehogs!',
		   	message,
		    '',
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



