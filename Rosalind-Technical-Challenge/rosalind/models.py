from django.db import models

# Create your models here.

#Initializing fields for new Teacher creation and reference db
class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length = 15)
    email = models.CharField(max_length = 50)
    birthday = models.DateField()
    class Meta:
        db_table="rosalind_teacher"

#Initializing fields for new Teacher's schedule and reference db
class TeacherSchedule(models.Model):
    teachers_name = models.CharField(max_length=100)
    teachers_schedule = models.CharField(max_length = 150)
    class Meta:
        db_table="rosalind_teacherschedule"
