from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rosalind.models import Teacher
from rosalind.models import TeacherSchedule
from rosalind.forms import TeacherForm, TeacherScheduleForm

# Create your views here.

#View of the homepage and teacher's schedules created
def index(request):
    showAllSchedules = TeacherSchedule.objects.all()
    return render(request, "index.html", {"data_set": showAllSchedules})

#View of teacher's schedules created
def showTeacherScheduleRegister(request):
    showAllSchedules = TeacherSchedule.objects.all()
    return render(request, "showTeacherScheduleRegister.html", {"data_set_2": showAllSchedules})

#View to showcase teacher's details after creation
def showTeacherRegister(request):
    showAllTeachers = Teacher.objects.all()
    return render(request, "showTeacherRegister.html", {"data": showAllTeachers})

#View of registering a new user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

#View of registering a new Teacher after login of admin user
def teacherRegisterInsert(request):
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('phone_number') and request.POST.get('email') and request.POST.get('birthday'):
            record = Teacher()
            record.fullname = request.POST.get('fullname')
            record.phone_number = request.POST.get('phone_number')
            record.email = request.POST.get('email')
            record.birthday = request.POST.get('birthday')
            record.save()
            return redirect('showTeacherRegister')
            #return render(request, "teacherRegister.html")
    else:
        return render(request, "teacherRegister.html")

#View of registering a Teacher's schedule after login of admin user
def teacherScheduleRegisterInsert(request):
    if request.method == "POST":
        if request.POST.get('teachers_name') and request.POST.get('teachers_schedule'):
            record = TeacherSchedule()
            record.teachers_name = request.POST.get('teachers_name')
            record.teachers_schedule = request.POST.get('teachers_schedule')
            record.save()
            return redirect('showTeacherScheduleRegister')
            #return render(request, "teacherScheduleRegister.html")
    else:
        return render(request, "teacherScheduleRegister.html")

#View to edit registered teacher's information
def editTeacherRegister(request, id):
    editTeacher = Teacher.objects.get(id=id)
    return render(request, "editTeacherRegister.html", {"Teacher": editTeacher})

#View to edit scheduled teacher's information
def editTeacherScheduleRegister(request, id):
    editTeacherSchedule = TeacherSchedule.objects.get(id=id)
    return render(request, "editTeacherScheduleRegister.html", {"TeacherSchedule": editTeacherSchedule})

#View to update Teacher Registration information
def updateTeacherRegister(request, id):
    updateTeacherRegister = Teacher.objects.get(id=id)
    form = TeacherForm(request.POST, instance=updateTeacherRegister)
    if form.is_valid():
        form.save()
        updateTeacherRegister=Teacher.objects.all()
    return redirect('showTeacherRegister')

    context = {'Teacher': updateTeacherRegister}
    return render(request, 'editTeacherRegister.html', context)

#View to update Teacher Schedule Registration Information
def updateTeacherScheduleRegister(request, id):
    updateTeacherScheduleRegister = TeacherSchedule.objects.get(id=id)
    form = TeacherScheduleForm(request.POST, instance=updateTeacherScheduleRegister)
    if form.is_valid():
        form.save()
        updateTeacherScheduleRegister=TeacherSchedule.objects.all()
    return redirect('showTeacherScheduleRegister')

    context = {'TeacherSchedule': updateTeacherScheduleRegister}
    return render(request, 'editTeacherScheduleRegister.html', context)

#View to delete Teacher Registration
def deleteTeacherRegister(request, id):
    Teacher.objects.filter(id=id).delete()
    return redirect('showTeacherRegister')

#View to delete Teacher schedule information
def deleteTeacherScheduleRegister(request, id):
    TeacherSchedule.objects.filter(id=id).delete()
    return redirect('showTeacherScheduleRegister')

