from django.contrib import admin
from .models import EndOfDayDataTable, CompanyFundamentalsTable, CompanyInfoTable

admin.site.register(EndOfDayDataTable)
admin.site.register(CompanyInfoTable)
admin.site.register(CompanyFundamentalsTable)

# Register your models here.
