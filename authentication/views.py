from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def Login(request):
    if request.user.is_authenticated:
        return redirect('/inventry/allproducts/')
    
    context ={
        'error' : ""
    }
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(request,username= request.POST['username'],
                            password=request.POST['password'])
        # print(user.role)

        if user is not None:
            login(request,user)
            if request.user.role == 0:
                return redirect ('/order/allcustomers/')
            elif request.user.role == 2:
                return redirect ('/order/vieworders/')
        else:
            context ={
                'error':"*Invalid user name and password"
            }
            return render( request,'login.html', context)

    return render (request,'login.html', context)

def LogoutUser(request):

    logout(request)
    return redirect('/')

def Signup(request):
    context = {
        'error': ""
    }
    if request.method == 'POST':
        user_check = User.objects.filter(username = request.POST['username'])
        if len(user_check) > 0:
            context = {
                'error' : "*Username Already exists"
            }
            return render (request,'signup.html',context)
        else:
            new_user = User(username = request.POST['username'],
                        first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        email = request.POST['email_address'],
                        age = request.POST['age'],
                        role = request.POST['role'])


            new_user.set_password(request.POST['password'])

            new_user.save()
        return redirect('/')

    return render (request,'signup.html',context)
