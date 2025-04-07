from django.contrib import admin
from .models import Driver
# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'national_id', 'tuk_tuk_number', 'latitude', 'longitude')