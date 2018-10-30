from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Daily_Price_Info, Company_Info, Time_Series, Fundamentals
from .serializers import Daily_Price_Info_Serializer, Company_Info_Serializer, Time_Series_Serializer, Fundamentals_Serializer

class dailyPriceInfoList(APIView):
	def get(self, request):
		dpi = Daily_Price_Info.objects.all()
		serializer = Daily_Price_Info_Serializer(dpi, many=True)
		return Response(serializer.data)	
	def post(self):
		pass

class companyInfoList(APIView):
	def get(self, request):
		cil = Company_Info.objects.all()
		serializer = Company_Info_Serializer(cil, many=True)
		return Response(serializer.data)	
	def post(self):
		pass

class timeSeriesList(APIView):
	def get(self, request):
		ts = Time_Series.objects.all()
		serializer = Time_Series_Serializer(ts, many=True)
		return Response(serializer.data)	
	def post(self):
		pass

class fundamentalsList(APIView):
	def get(self, request):
		fs = Time_Series.objects.all()
		serializer = Fundamentals_Serializer(fs, many=True)
		return Response(serializer.data)	
	def post(self):
		pass
# Create your views here.
