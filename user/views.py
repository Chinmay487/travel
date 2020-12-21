from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User

# Create your views here.

def loginPage(request):
    return render(request,'login.html')

def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is None:
        return redirect('/')

    auth.login(request,user)
    return redirect('/manage/')
