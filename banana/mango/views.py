from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import EmployeeForm
from .models import Employee


def home(request):
   return render(request,'home.html')

def index(request):
    employee=Employee.objects.all()
    details={'emp_data':employee}
    return render(request,'index.html',details)

def create(request):
    if request.method=='POST':
        print(request.POST)
        form=EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/chittoor/')
    else:
            form=EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request,id):
    emp_data = Employee.objects.get(id=id)
    form=EmployeeForm(instance=emp_data)
    return render(request,"update.html",{'form':form,'id':id})

def update(request,id):
    emp_data = Employee.objects.get(id=id)
    form= EmployeeForm(request.POST,instance=emp_data)
    if form.is_valid():
        form.save()
        return redirect('/chittoor/')
    return render(request,"update.html", {'form':form,'id':id})

def delete(request,id):
    emp_data=Employee.objects.get(id=id)
    emp_data.delete()
    return redirect('/chittoor/')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        print(user)
        if user:
            return redirect('/chittoor/')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')
