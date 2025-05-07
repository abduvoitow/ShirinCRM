from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import DateInput

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'start_date', 'end_date', 'days', 'time']
        widgets = {
            'start_date': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Formatni to'g'rilab qo'yamiz, qiymat ko'rinishi uchun
        if self.instance and self.instance.start_date:
            self.initial['start_date'] = self.instance.start_date.strftime('%Y-%m-%d')
        if self.instance and self.instance.end_date:
            self.initial['end_date'] = self.instance.end_date.strftime('%Y-%m-%d')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'phone', 'passport_series', 'passport_number', 'jshr']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['is_present']



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)