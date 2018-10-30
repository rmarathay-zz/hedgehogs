from rest_framework import serializers
from .models import Daily_Price_Info, Company_Info, Time_Series, Fundamentals


class Daily_Price_Info_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Daily_Price_Info
		fields = '__all__'

class Company_Info_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Company_Info
		fields = '__all__'

class Time_Series_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Time_Series
		fields = '__all__'  

class Fundamentals_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Fundamentals
		fields = '__all__'