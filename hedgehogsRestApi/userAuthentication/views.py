from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def userauthpage(request):
	return render(request, 'userAuthentication/userauth.html', {})