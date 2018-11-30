from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def aboutpage(request):
	print("this works!");
	return render(request, 'about/about.html')
	#return HttpResponse("This is working")