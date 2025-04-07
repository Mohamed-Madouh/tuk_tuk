from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Loginform, Registerform, AccountConfirmationForm
from django.contrib import messages
from django.core.mail import send_mail
from .models import CustomUser
import random

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "البريد الإلكتروني أو كلمة المرور غير صحيحة.")
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Input validation
        if not email or not password:
            messages.error(request, "يرجى إدخال البريد الإلكتروني وكلمة المرور.")
            return render(request, 'register.html')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم بالفعل.")
            return render(request, 'register.html')
        if phone and CustomUser.objects.filter(phone_number=phone).exists():
            messages.error(request, "رقم الهاتف مستخدم بالفعل.")
            return render(request, 'register.html')

        try:
            # Create the user
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone,
                email=email,
                password=password
            )
            messages.success(request, "تم إنشاء الحساب بنجاح!")
            return redirect('home')  # Redirect to the home page
        except Exception as e:
            messages.error(request, f"حدث خطأ أثناء إنشاء الحساب: {str(e)}")
            return render(request, 'register.html')

    return render(request, 'register.html')

def forgot_password(request):
    if request.method == "POST":
        form = AccountConfirmationForm(request.POST)
        if form.is_valid():
            phone_or_email = form.cleaned_data['phone_or_email']
            code = str(random.randint(1000, 9999))
            try:
                user = CustomUser.objects.get(email=phone_or_email)
                user.profile.reset_code = code
                user.profile.save()

                request.session['email'] = phone_or_email  # Store email in session
                send_mail(
                    "Account Confirmation Code",
                    f"Your confirmation code is: {code}",
                    "admin@example.com",
                    [phone_or_email],
                )
                messages.success(request, "تم إرسال الكود إلى البريد الإلكتروني.")
                return redirect('verify_code')
            except CustomUser.DoesNotExist:
                messages.error(request, "تعذر العثور على الحساب. يرجى التحقق من البيانات.")
            except Exception as e:
                messages.error(request, "تعذر إرسال الكود، يرجى المحاولة لاحقاً.")
        else:
            messages.error(request, "يرجى التحقق من رقم الهاتف أو البريد الإلكتروني.")
    else:
        form = AccountConfirmationForm()
    return render(request, 'forgot_password.html', {'form': form})

def verify_code(request):
    if request.method == "POST":
        code = request.POST.get('code')  # الحصول على الكود المدخل
        email = request.session.get('email')  # حفظ البريد في الجلسة مسبقًا أثناء الإرسال
        
        if not email:
            messages.error(request, "حدث خطأ. يرجى المحاولة مرة أخرى.")
            return redirect('forgot_password')
        
        try:
            user = CustomUser.objects.get(email=email)
            if hasattr(user, 'profile') and user.profile.reset_code == code:
                messages.success(request, "تم التحقق بنجاح. يمكنك الآن إعادة تعيين كلمة المرور.")
                return redirect('reset_password')  # رابط صفحة إعادة تعيين كلمة المرور
            else:
                messages.error(request, "الكود غير صحيح.")
        except CustomUser.DoesNotExist:
            messages.error(request, "حدث خطأ أثناء التحقق. يرجى المحاولة مجددًا.")
    
    return render(request, 'verify_code.html')

def reset_password(request):
    """إعادة تعيين كلمة المرور"""
    if request.method == 'POST':
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        # التحقق من تطابق كلمتي المرور
        if new_password != confirm_password:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
        else:
            # تحديث كلمة المرور للمستخدم الحالي
            user = request.user
            user.set_password(new_password)
            user.save()
            messages.success(request, "تم تحديث كلمة المرور بنجاح!")
            return redirect('login')  # إعادة التوجيه إلى صفحة تسجيل الدخول

    return render(request, 'reset_password.html')


