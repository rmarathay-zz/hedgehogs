from django.contrib import admin
from .models import Daily_Price_Info, Company_Info, Time_Series, Fundamentals

admin.site.register(Daily_Price_Info)
admin.site.register(Company_Info)
admin.site.register(Time_Series)
admin.site.register(Fundamentals)

# Register your models here.
