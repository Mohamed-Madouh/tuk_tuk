from django.contrib import admin
from .models import PasswordReset , Profile , CustomUser

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(PasswordReset)