from django.db import models

class Driver(models.Model):
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    name = models.CharField(max_length=100, verbose_name="اسم السائق")
    phone_number = models.CharField(max_length=11, verbose_name="رقم الهاتف")
    national_id = models.CharField(max_length=14, unique=True, verbose_name="الرقم القومي")
    tuk_tuk_number = models.CharField(max_length=20, unique=True, verbose_name="رقم التوك توك")
    latitude = models.FloatField(verbose_name="خط العرض", null=True, blank=True)
    longitude = models.FloatField(verbose_name="خط الطول", null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="آخر تحديث")

    def __str__(self):
        return self.name

class DriverRoute(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="routes")
    latitude = models.FloatField(verbose_name="خط العرض")
    longitude = models.FloatField(verbose_name="خط الطول")
    speed = models.FloatField(verbose_name="السرعة (كم/ساعة)", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="وقت التسجيل")

    def __str__(self):
        return f"Route for {self.driver.name} at {self.timestamp}"
