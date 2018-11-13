from rest_framework import serializers
from .models import EndOfDayDataTable, CompanyFundamentalsTable, CompanyInfoTable


class company_fundamentals_serializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyFundamentalsTable
		fields = '__all__'

class company_info_serializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyInfoTable
		fields = '__all__'

class end_of_day_data_serializer(serializers.ModelSerializer):
	class Meta:
		model = EndOfDayDataTable
		fields = '__all__'

