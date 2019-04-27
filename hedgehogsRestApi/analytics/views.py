from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from social_django.models import UserSocialAuth
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EndOfDayDataTable, CompanyFundamentalsTable, CompanyInfoTable
from .serializers import end_of_day_data_serializer, company_info_serializer, company_fundamentals_serializer


class companyInfoList(APIView):
	def get(self, request):
		dpi = CompanyInfoTable.objects.all()
		serializer = company_info_serializer(dpi, many=True)
		return Response(serializer.data)	
	def post(self):
		pass

class companyFundamentalsList(APIView):
	def get(self, request):
		dpi = CompanyFundamentalsTable.objects.all()
		serializer = company_fundamentals_serializer(dpi, many=True)
		return Response(serializer.data)	
	def post(self):
		pass

class endOfDataList(APIView):
	def get(self, request):
		dpi = EndOfDayDataTable.objects.all()
		serializer = end_of_day_data_serializer(dpi, many=True)
		return Response(serializer.data)	
	def post(self):
		pass

# Create your views here.
