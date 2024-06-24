from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import District, branch
# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,'password miss match')
            return redirect('/register')
    return render(request,"register.html")           
            
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/new')
        else:
            messages.info(request,'invalid login')
            return redirect('/login')
    return render(request,'login.html')   
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    if request.method == 'POST':
        return redirect('/')
    return render(request,"new.html")

def getdata(request):
    district=District.objects.all()
    branches=branch.objects.all()
    if request.method == 'POST':
        return redirect('/')
    return render(request, "profile.html", {'District': district, 'branch': branches})


   