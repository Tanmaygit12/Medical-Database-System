from django.contrib import admin
from .models import Student
from .models import Patient
from .models import Appointment
# Register your models here.
admin.site.register(Student)
admin.site.register(Patient)
admin.site.register(Appointment)