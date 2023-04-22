from pydoc import doc
from django.shortcuts import render,redirect
from .models import Student
from .models import Patient
from .models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pnumber = request.POST.get('pnumber')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        eventName = request.POST.get('event')
        time = request.POST.get('time')
        date = request.POST.get('date')
        student = Student(fname = fname, lname = lname, pnumber = pnumber, username = username, email = email, password = password, age = age, eventName = eventName, time = time, date = date)
        student.save()
        user = User.objects.create_user(username, email, password)
        user.save()

    return render(request, ('SignUpPage.html'))

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/mainPage")
        else:
            return render(request, ('LoginPage.html'))
            
    return render(request, ('LoginPage.html'))

def logoutUser(request):
    logout(request)
    return redirect("/login")

def mainPage(request):
    if request.method == "POST":
        hname = request.POST.get('hname')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        bp = request.POST.get('bp')
        sl = request.POST.get('sl')
        dw = request.POST.get('dw')
        li = request.POST.get('li')
        admitdate = request.POST.get('admitdate')
        dischargedate = request.POST.get('dischargedate')
        patient = Patient(hname=hname, doctor=doctor, date=date, bp=bp, sl=sl, dw=dw, li=li, admitdate=admitdate, dischargedate=dischargedate)
        patient.save()
        
    return render(request, ('ProfilePage.html'))

def form(request):
    return render(request, ('Form.html'))

def appointment(request):
    if request.method == "POST":
        pname = request.POST.get('pname')
        hname = request.POST.get('hname')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        appointment = Appointment(pname=pname, hname=hname, doctor=doctor, date=date, time=time)
        appointment.save()

    return render(request, ('Appointment.html'))



