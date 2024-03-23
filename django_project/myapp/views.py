from typing import Any
from django.shortcuts import HttpResponse,render,redirect
from .forms import SignUpForm
from .models import animal,deceased,sold
from django.db.models import Q
from .tables import *
from base import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
import os
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.

@login_required(login_url='login')
def add_record(request):
    
    if request.method == 'POST':
        
        
        animal_code = request.POST.get('code')
        animal_parent = request.POST.get('parent')
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
                image = animal_image,
                parent = animal_parent
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
                image = 'default.jpg',
                parent = animal_parent
            )
            messages.success(request,"Record added!")
            return redirect('add')
             
    
    return render(request, 'add_record.html')

@login_required(login_url='login')
def update_record(request,pk):
    record = animal.objects.get(id=pk)

    old_image = record.image
    
    if request.method == 'POST':
        
        record.code = request.POST.get('code')
        record.number = request.POST.get('number')
        record.date = request.POST.get('date')
        record.gender = request.POST.get('gender')
        if request.FILES.get('image') is not None:
            record.image = request.FILES.get('image') 
        record.parent = request.POST.get('parent')
        record.save()

        if str(record.image) != str(old_image) and old_image != 'default.jpg':
             
             file_path = os.path.join(settings.MEDIA_ROOT,str(old_image))
             
             if os.path.exists(file_path):
                
                os.remove(file_path)

       
        
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
    
    RequestConfig(request, paginate={"per_page": 3}).configure(table)
    return render(request,'list_new.html',context={'table':table})


def deceasedAnimal(request,pk):
     
    record = animal.objects.get(id=pk)
    if request.method == 'POST':
        
        deceased.objects.create(
            parent = record.parent,
            user = record.user,
            code = record.code,
            number = record.number,
            gender = record.gender,
            date = record.date,
            cause = request.POST.get('cause'),
            image = record.image
        )
        messages.success(request,'Record added to deceased list')
        return redirect('list')
    return render(request,'deceased.html')

def sell(request,pk):
     
    record = animal.objects.get(id=pk)
    if request.method == 'POST':
        
        sold.objects.create(
            parent = record.parent,
            user = record.user,
            code = record.code,
            number = record.number,
            date = record.date,
            price = request.POST.get('price'),
            sold_to = request.POST.get('code'),
            gender = record.gender,
            image = record.image
        )
        messages.success(request,'Record sold!')
        return redirect('list')
    return render(request,'sold.html')

def viewSold(request):
     records = sold.objects.all()
     return render(request,'viewSold.html',{'records':records})

def bootstrap_list(request):
    list = request.POST.getlist('selected')
    
    current_page = int(request.GET.get('page')) if request.GET.get('page') is not None else 1
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    records = animal.objects.filter(user=request.user).filter(
        Q(code__icontains=q) |
        Q(date__icontains=q) |
        Q(gender__icontains=q) |
        Q(number__icontains=q) 
    )
    paginator = Paginator(records,3)
    print(type(current_page))
    print(f"current page {current_page}")
    
    records = paginator.get_page(current_page)
    print(f'records = {records}')
    num_of_pages = paginator.num_pages
    print(type(num_of_pages))
    print(f'range of numofpages {range(num_of_pages)}')
    # query all records
    #if request = post then filter q
    #then paginate records
    
    if request.method == 'POST':
        if request.POST.get('check') is not None:
            
            print(list)
        elif request.POST.get('delete'):
            for i in list:
                record = animal.objects.get(id=i)
                record.delete()
            
    previous = current_page - 1
    next = current_page + 1

    context = {'records':records,'range':range(1,num_of_pages+1),
               'previous':previous,'next':next,'current':current_page,               
               'lastpage':num_of_pages}
    return render(request,'bootstrap-list.html',context)


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
    full_record_number = animal_record.code + animal_record.number
    cubs = animal.objects.filter(parent=full_record_number)
    if request.user == animal.objects.get(id=pk).user:

        return render(request,'viewrecord.html',context={'animal_record':animal_record,'cubs':cubs})
    else:
        raise Http404
    
    


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


