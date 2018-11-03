from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import os

BASE_DIR = os.path.realpath('.')

def homepage(request):
	return render(request, BASE_DIR+'/templates/homepage/homepage.html')

