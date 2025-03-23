
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.street +" "+ str(self.number)

class School(models.Model):
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    principal = models.CharField(max_length=100)
    number_of_employees = models.PositiveIntegerField()
    number_of_students = models.PositiveIntegerField()
    date_founded = models.DateField()
    added_by = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name +", "+ str(self.date_founded)


class Subject (models.Model):

    CLASS_CHOICE =[
        ("1","First"),
        ("2","Second"),
        ("3","Third"),
        ("4","Fourth"),
        ("5","Fifth"),
    ]
    name = models.CharField(max_length=100)
    class_n = models.CharField(max_length=100,choices=CLASS_CHOICE)
    school = models.ForeignKey(School,on_delete=CASCADE)

    def __str__(self):
        return self.name

class Teacher (models.Model):
    name = models.CharField(max_length=100)
    surname =models.CharField(max_length=100)
    ssn = models.IntegerField()
    salary = models.IntegerField()
    added_by = models.ForeignKey(User,on_delete=CASCADE)
    school = models.ForeignKey(School,on_delete=CASCADE)

    def __str__(self):
        return self.name +" "+ self.surname

class Student (models.Model):
    name = models.CharField(max_length=100)
    surname =models.CharField(max_length=100)
    date_of_birth = models.DateField()
    current_class = models.IntegerField()
    parent_phone_number = models.PositiveIntegerField()
    added_by = models.ForeignKey(User,on_delete=CASCADE)
    school = models.ForeignKey(School, on_delete=CASCADE)

    def __str__(self):
        return self.name +" "+ self.surname


class TeacherSubject (models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=CASCADE)
    subject = models.ForeignKey(Subject,on_delete=CASCADE)

    def __str__(self):
        return str(self.teacher) +" teaches "+ str(self.subject)