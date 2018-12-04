from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class CompanyFundamentalsTable(models.Model):
    c_id = models.UUIDField(blank=True, null=True)
    indicator = models.TextField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    ticker = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'fundamentals_sample'


class CompanyInfoTable(models.Model):
    company_id = models.TextField(primary_key=True)
    ticker = models.TextField(blank=True, null=True)
    ticker_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'company_info_table'

class EndOfDayDataTable(models.Model):
    primary_key = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=7, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'end_of_day_data_table'

class EodCompanyRelation(models.Model):
    company_info = models.OneToOneField(
        CompanyInfoTable, 
        on_delete = models.CASCADE, 
        primary_key = True,
    )
    

    def __str__(self):
        return str(company_info.ticker)