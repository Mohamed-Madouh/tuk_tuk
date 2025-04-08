from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # الصفحة الرئيسية
    path('driver/', views.driver_list, name='driver_list'),
    path('driver/add/', views.add_driver, name='add_driver'),
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('driver/<int:driver_id>/update-location/', views.update_driver_location, name='update_driver_location'),
    path('driver/<int:driver_id>/routes/', views.get_driver_routes, name='get_driver_routes'),
    path('logout/', views.logout_view, name='logout'),
]