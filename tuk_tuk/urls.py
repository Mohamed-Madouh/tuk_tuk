from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # الصفحة الرئيسية
    path('driver/', views.driver_list, name='driver_list'),
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('driver/add/', views.add_driver, name='add_driver'),
    path('logout/', views.logout_view, name='logout'),
]