from django.shortcuts import render ,redirect   , get_object_or_404
from django.contrib import messages
from .models import Driver
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def driver_list(request):
    """عرض قائمة السائقين"""
    drivers = Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    """عرض تفاصيل السائق مع موقعه على الخريطة"""
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'driver_detail.html', {'driver': driver})

def add_driver(request):
    """إضافة سائق جديد"""
    if request.method == 'POST':
        # استخراج البيانات من الفورم
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        national_id = request.POST.get('national_id')
        tuk_tuk_number = request.POST.get('tuk_tuk_number')
        latitude = request.POST.get('latitude', None)  # السماح بترك خط العرض فارغاً
        longitude = request.POST.get('longitude', None)  # السماح بترك خط الطول فارغاً

        # التحقق من صحة البيانات
        if not all([name, phone_number, national_id, tuk_tuk_number]):
            messages.error(request, "يرجى ملء جميع الحقول الإلزامية.")
            return render(request, 'add_driver.html')
        
        if not phone_number.isdigit() or len(phone_number) != 11:
            messages.error(request, "رقم الهاتف يجب أن يتكون من 11 رقمًا.")
            return render(request, 'add_driver.html')

        if not national_id.isdigit() or len(national_id) != 14:
            messages.error(request, "الرقم القومي يجب أن يتكون من 14 رقمًا.")
            return render(request, 'add_driver.html')

        if Driver.objects.filter(national_id=national_id).exists():
            messages.error(request, "الرقم القومي موجود بالفعل.")
            return render(request, 'add_driver.html')

        if Driver.objects.filter(tuk_tuk_number=tuk_tuk_number).exists():
            messages.error(request, "رقم التوك توك موجود بالفعل.")
            return render(request, 'add_driver.html')

        # إدخال البيانات في قاعدة البيانات
        try:
            Driver.objects.create(
                name=name,
                phone_number=phone_number,
                national_id=national_id,
                tuk_tuk_number=tuk_tuk_number,
                latitude=latitude,
                longitude=longitude
            )
            messages.success(request, "تم إضافة السائق بنجاح!")
            return redirect('driver_list')  # إعادة التوجيه إلى قائمة السائقين
        except Exception as e:
            messages.error(request, f"حدث خطأ أثناء حفظ البيانات: {str(e)}")
            return render(request, 'add_driver.html')

    return render(request, 'add_driver.html')




@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')