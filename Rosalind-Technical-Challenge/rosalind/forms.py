from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rosalind.models import Teacher, TeacherSchedule

#Initialize fields for new user registration for register page
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

#Initialized fields for Teacher form
class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"

#Initialized fields for Teacher Schedule Form
class TeacherScheduleForm(forms.ModelForm):
    class Meta:
        model=TeacherSchedule
        fields="__all__"