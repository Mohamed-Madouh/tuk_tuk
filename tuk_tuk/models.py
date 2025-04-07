from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم السائق")
    phone_number = models.CharField(max_length=11, verbose_name="رقم الهاتف")
    national_id = models.CharField(max_length=14, unique=True, verbose_name="الرقم القومي")
    tuk_tuk_number = models.CharField(max_length=20, unique=True, verbose_name="رقم التوك توك")
    latitude = models.FloatField(verbose_name="خط العرض", null=True, blank=True)
    longitude = models.FloatField(verbose_name="خط الطول", null=True, blank=True)

    

    def __str__(self):
        return self.name