from django import forms
from .models import Driver  # تأكد من وجود الموديل DriverData

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver  # الموديل المرتبط
        fields = ['name', ' national_id ','tuk_tuk_number','phone_number', 'latitude', 'longitude']
        def clean_phone_number(self):
            
            phone_number = self.cleaned_data.get('phone_number')
             
            if not phone_number.isdigit():
               raise forms.ValidationError("رقم الهاتف يجب أن يحتوي على أرقام فقط.")
            return phone_number
