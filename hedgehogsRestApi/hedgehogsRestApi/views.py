from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def homepage(request):
	return render(request, 'homepage/homepage.html')

def graph_search(request):
	if request.method == 'GET':
		req = request.GET.get('search_box', None)
		print(req)
		return render(request, "about/about.html")
	else:
		print("It's a get request!\n")
	return render(request, "about/about.html")