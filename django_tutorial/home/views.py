from django.shortcuts import render
from django.http import HttpResponse
from . models import Department,Doctors
from . forms import BookingForm
# Create your views here.

def index(request):
    person={
        'num1':11,
    }

    return render(request,'index.html' ,person)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method =="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form= BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_doct= {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doct)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept':Department.objects.all(),
    }
    return render(request,'department.html',dict_dept)

