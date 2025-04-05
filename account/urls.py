from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),  # تأكد من إضافة هذا النمط
    path('verify_code/', views.verify_code, name='verify_code'),  # تأكد من إضافة هذا النمط
    path('reset_password/', views.reset_password, name='reset_password'),  # تأكد من إضافة هذا النمط
]