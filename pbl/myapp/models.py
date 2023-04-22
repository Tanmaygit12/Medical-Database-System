from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    pnumber = models.CharField(max_length=10)
    username = models.CharField(max_length=100, default='mayur')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)
    age = models.IntegerField(default=20)
    eventName = models.CharField(max_length=100, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

class Patient(models.Model):
    hname = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    bp = models.CharField(max_length=100)
    sl = models.CharField(max_length=100)
    dw = models.CharField(max_length=100)
    li = models.CharField(max_length=100)
    admitdate = models.CharField(max_length=100)
    dischargedate = models.CharField(max_length=100)

class Appointment(models.Model):
    pname = models.CharField(max_length=100)
    hname = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.TimeField()
    


    

