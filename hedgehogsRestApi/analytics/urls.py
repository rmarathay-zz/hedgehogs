from django.urls import path
from . import views

urlpatterns = [
	path('company_info/', views.companyInfoList.as_view(), name = "company_info"),
	path('company_fundamentals/', views.companyFundamentalsList.as_view(), name = "company_fundamentals"),
	path('end_of_day_data/',  views.endOfDataList.as_view(), name= "end_of_day_data"),
]