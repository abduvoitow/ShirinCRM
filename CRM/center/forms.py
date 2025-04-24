from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'course_name', 'start_date', 'end_date', 'days', 'time']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'format': 'd.m.Y'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'format': 'd.m.Y'}),
        }

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