from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def Home(request):
    
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()
        
    data = Employee.objects.all()
    
    context = {
        
        'form':form,
        'data':data
        
    }
    return render(request,'app1/index.html',context)

def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')
    
    
def Update_Record(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context)    


def sign_up(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
    
        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                
                messages.info(request, 'This username alredy exists!!')
                
            else:
                
                User.objects.create_user(username=username,email=email, password=password1)
                return redirect('login')
                
        else: 
            messages.info(request, 'Passwords are not same!!')
    
    
            
    return render( request , 'app1/signup.html')


def sign_in(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        
        user =  authenticate(username=username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        
    
    return render( request, 'app1/login.html')



def log_out(request):
    
    logout(request)
    
    return redirect('login')
