# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnalyticsCompanyInfo(models.Model):
    """stores company info including id, ticker,companyname"""
    company_id = models.FloatField()
    ticker = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'analytics_company_info'


class AnalyticsDailyPriceInfo(models.Model):
    """stores infomation about the price values and data"""
    data = models.CharField(max_length=250)
    open_data = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    percent_change = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField()
    week_high_52 = models.FloatField()
    week_low_52 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'analytics_daily_price_info'


class AnalyticsFundamentals(models.Model):
    """stores information about fundementals data"""
    c_id = models.FloatField()
    company_name = models.CharField(max_length=250)
    common_shares_outstanding = models.FloatField()
    close = models.FloatField()
    date = models.DateTimeField()
    high = models.FloatField()
    low = models.FloatField()
    open_data = models.FloatField()
    percent_change = models.FloatField()
    price = models.FloatField()
    volume = models.FloatField()
    week_high_52 = models.FloatField()
    week_low_52 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'analytics_fundamentals'


class AnalyticsTimeSeries(models.Model):
    """stores time related fields"""
    ts_id = models.FloatField()
    company_id = models.FloatField()
    ticker = models.CharField(max_length=250)
    price = models.FloatField()
    date = models.DateTimeField()
    open_data = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()

    class Meta:
        """meta class"""
        managed = False
        db_table = 'analytics_time_series'


class AuthGroup(models.Model):
    """Authentication field"""
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    """permissions field"""
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    """user authentication class"""
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    """user authentication data"""
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        """meta class"""
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    """authentication groups"""
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    """user permissions class"""
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CompanyFundamentalsTable(models.Model):
    """company fundementals data table values"""
    c_id = models.UUIDField(blank=True, null=True)
    indicator = models.TextField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    ticker = models.TextField(blank=True, null=True)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'company_fundamentals_table'


class CompanyInfoTable(models.Model):
    """company infromation values class"""
    company_id = models.TextField(primary_key=True)
    ticker = models.TextField(blank=True, null=True)
    ticker_id = models.TextField(blank=True, null=True)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'company_info_table'


class DjangoAdminLog(models.Model):
    """django admin class"""
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    """Django content type modle values"""
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    """Migrations class for app models"""
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        """meta class"""
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    """Django session class values"""
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        """meta class"""
        managed = False
        db_table = 'django_session'


class EndOfDayDataTable(models.Model):
    """end of day table values"""
    primary_key = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=7, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'end_of_day_data_table'


class Test(models.Model):
    """test class values"""
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        """meta class"""
        managed = False
        db_table = 'test'
