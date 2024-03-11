from typing import Any
from django.shortcuts import HttpResponse,render,redirect
from .forms import SignUpForm
from .models import animal
from django.db.models import Q
from .tables import *
from base import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
import os

# Create your views here.

@login_required(login_url='login')
def add_record(request):
    
    if request.method == 'POST':
        
        
        animal_code = request.POST.get('code')
        animal_date = request.POST.get('date')
        animal_gender = request.POST.get('gender')
        animal_number = request.POST.get('number')
        animal_image = request.FILES.get('image')
        
        if animal.objects.filter(code=animal_code,number=animal_number):
            messages.error(request,'Record already exists!')
            return redirect('add')
        elif animal_image is not None:
            animal.objects.create(
                user = request.user,
                code = animal_code,
                date = animal_date,
                gender = animal_gender,
                number = animal_number,
                image = animal_image
            )
            messages.success(request,"Record added!")
            return redirect('add')
        else:
            animal.objects.create(
                user = request.user,
                code = animal_code,
                date = animal_date,
                gender = animal_gender,
                number = animal_number,
                image = 'default.jpg'
            )
            messages.success(request,"Record added!")
            return redirect('add')
             
    
    return render(request, 'add_record.html')

@login_required(login_url='login')
def update_record(request,pk):
    record = animal.objects.get(id=pk)

    old_image = record.image
    print(os.listdir(settings.MEDIA_ROOT))
    if request.method == 'POST':
        
        record.code = request.POST.get('code')
        record.number = request.POST.get('number')
        record.date = request.POST.get('date')
        record.gender = request.POST.get('gender')
        record.image = request.FILES.get('image')
        
        record.save()

        if str(record.image) != str(old_image) and old_image != 'default.jpg':
             print(str(record.image) + '  ' + str(old_image))
             file_path = os.path.join(settings.MEDIA_ROOT,str(old_image))
             print(file_path)
             if os.path.exists(file_path):
                print("yey")
                os.remove(file_path)

        print(os.listdir(settings.MEDIA_ROOT))
        
        return redirect('list')
    
       
    else:
        return render(request,'update_record.html',{'animal_record':record})
@login_required(login_url='login')
def delete_record(request,pk):
     
    record = animal.objects.get(id=pk)
    file_path = os.path.join(settings.MEDIA_ROOT,str(record.image))
        
    if os.path.exists(file_path) and record.image != 'default.jpg':
        
        os.remove(file_path)
    record.delete()

    return redirect('list')

@login_required(login_url='login')
def animal_listing(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    table = testTable(data=animal.objects.filter(user_id=request.user.pk).filter(
        Q(code__icontains=q) |
        Q(date__icontains=q) |
        Q(gender__icontains=q) |
        Q(number__icontains=q) 


    ))
    
    RequestConfig(request, paginate={"per_page": 15}).configure(table)
    return render(request,'list_new.html',context={'table':table})




def bootstrap_list(request):
     
     records = animal.objects.all()

     return render(request,'bootstrap-list.html',{'records':records})


def home(request):
   
    return render(request,'home.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,username=email,password=password)

        if user is not None:
        
            login(request,user)
            messages.success(request,"You have logged in")
            return redirect('home')
        else:
            messages.error(request,"Username or password does not exist")
            return redirect('home')
    else:
        
        return render(request,'login.html')
    
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request,'You have logged out')
    return redirect('home')

@login_required(login_url='login')
def viewRecord(request,pk):

    animal_record = animal.objects.get(id=pk)
    
    
    return render(request,'viewrecord.html',context={'animal_record':animal_record})


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			user = authenticate(username=email, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


