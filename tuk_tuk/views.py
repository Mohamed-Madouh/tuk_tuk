from django.shortcuts import render ,redirect   , get_object_or_404
from django.contrib import messages
from .models import Driver, DriverRoute
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json

  # Import the requests module
# Create your views here.

def driver_list(request):
    """عرض قائمة السائقين"""
    drivers = Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    """عرض تفاصيل السائق مع موقعه على الخريطة"""
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'driver_detail.html', {'driver': driver})
def fetch_location(phone_number):
    """Fetch latitude and longitude from an API using phone number."""
    api_url = "https://example.com/location-api"  # Replace with actual API URL
    params = {"phone_number": phone_number}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("latitude"), data.get("longitude")
    return None, None
def add_driver(request):
    """إضافة سائق جديد إلى قاعدة البيانات."""
    if request.method == "POST":
        # استخراج البيانات من الطلب
        name = request.POST.get('driverName')
        phone_number = request.POST.get('driverPhone')
        national_id = request.POST.get('nationalId')
        tuk_tuk_number = request.POST.get('tukTukNumber')

        # تحقق من صحة البيانات
        if not all([name, phone_number, national_id, tuk_tuk_number]):
            messages.error(request, "يرجى ملء جميع الحقول.")
            return render(request, 'add_driver.html')

        # التحقق من عدم وجود تكرار في الرقم القومي أو رقم التوكتوك
        if Driver.objects.filter(national_id=national_id).exists():
            messages.error(request, "الرقم القومي موجود بالفعل.")
            return render(request, 'add_driver.html')
        if Driver.objects.filter(tuk_tuk_number=tuk_tuk_number).exists():
            messages.error(request, "رقم التوك توك موجود بالفعل.")
            return render(request, 'add_driver.html')

        # إنشاء السائق الجديد
        try:
            Driver.objects.create(
                name=name,
                phone_number=phone_number,
                national_id=national_id,
                tuk_tuk_number=tuk_tuk_number
            )
            messages.success(request, "تمت إضافة السائق بنجاح!")
            return redirect('driver_list')  # إعادة التوجيه إلى صفحة قائمة السائقين
        except Exception as e:
            messages.error(request, f"حدث خطأ أثناء الحفظ: {str(e)}")
            return render(request, 'add_driver.html')

    return render(request, 'add_driver.html')
@csrf_exempt
def update_driver_location(request, driver_id):
    """تحديث موقع السائق وتسجيل خط السير."""
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            speed = data.get('speed')  # استلام السرعة من الطلب

            if latitude and longitude:
                # تحديث الموقع الحالي
                driver.latitude = float(latitude)
                driver.longitude = float(longitude)
                driver.save()

                # تسجيل الموقع الجديد في خط السير
                DriverRoute.objects.create(driver=driver, latitude=latitude, longitude=longitude, speed=speed)

                return JsonResponse({"status": "success", "message": "تم تحديث الموقع وتسجيل خط السير!"})
            else:
                return JsonResponse({"status": "error", "message": "إحداثيات غير صالحة."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "طلب غير صالح."})

def get_driver_routes(request, driver_id):
    """إرجاع خط السير للسائق."""
    driver = get_object_or_404(Driver, id=driver_id)
    routes = driver.routes.all().order_by('timestamp')  # جلب خط السير بالترتيب الزمني
    route_data = [{"latitude": route.latitude, "longitude": route.longitude, "speed": route.speed} for route in routes]

    return JsonResponse({"routes": route_data})
    return JsonResponse({"routes": route_data})
@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')
def driver_detail(request, driver_id):
    """عرض تفاصيل السائق مع موقعه على الخريطة."""
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'driver_detail.html', {'driver': driver})