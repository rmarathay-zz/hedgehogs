from django.urls import path
from . import views

urlpatterns = [
	path('daily_price_info/', views.dailyPriceInfoList.as_view(), name = "daily_price_info"),
	path('company_info/', views.companyInfoList.as_view(), name = "company_info"),
	path('time_series/', views.timeSeriesList.as_view(), name = "time_series"),	
	path('fundamentals/', views.fundamentalsList.as_view(), name= "fundamentals"),
]