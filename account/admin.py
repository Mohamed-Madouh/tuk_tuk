from django.contrib import admin
from .models import passwrodReset , Profile , CustomUser

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(passwrodReset)