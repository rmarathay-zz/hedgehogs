from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def toolspage(request):
	return render(request, 'tools/tools.html,', {})