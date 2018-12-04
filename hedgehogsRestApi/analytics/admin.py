from django.contrib import admin
from .models import EndOfDayDataTable, CompanyFundamentalsTable, CompanyInfoTable, EodCompanyRelation

admin.site.register(EndOfDayDataTable)
admin.site.register(CompanyInfoTable)
admin.site.register(CompanyFundamentalsTable)
admin.site.register(EodCompanyRelation)

# Register your models here.
