from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class Loginform(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
class Registerform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # استخدم `password1` من الحقول المحددة
        if commit:
            user.save()
        return user

    def clean_password(self):
        password = self.cleaned_data['password1']
        if len(password) < 8:
            raise forms.ValidationError('كلمة المرور يجب أن تكون 8 أحرف على الأقل')
        return password
    
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Enter your email")

    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('هذا البريد غير مسجل')
        return email

class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    
class AccountConfirmationForm(forms.Form):
    phone_or_email = forms.CharField(
        label="رقم الهاتف أو البريد الإلكتروني",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'رقم الهاتف أو البريد الإلكتروني'})
    )