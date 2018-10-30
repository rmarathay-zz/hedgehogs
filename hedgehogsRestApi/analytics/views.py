from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Daily_Price_Info
from . models import Company_Info
from . models import Time_Series
from . models import Fundamentals
from .serializers import Daily_Price_Info_Serializer

class dailyPriceInfoList(APIView):
	def get(self, request):
		dpi = Daily_Price_Info.objects.all()
		serializer = Daily_Price_Info_Serializer(dpi, many=True)
		return Response(serializer.data)	
	def post(self):
		pass
# Create your views here.
