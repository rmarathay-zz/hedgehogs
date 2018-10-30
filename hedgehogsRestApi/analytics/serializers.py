from rest_framework import serializers
from .models import Daily_Price_Info

class Daily_Price_Info_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Daily_Price_Info
		fields = '__all__'