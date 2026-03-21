from django.shortcuts import render,redirect
# from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def LoginPage(request):
    context={
        'error':''
    }
    if request.method == "POST":
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        print(user)
    
        if user is not None:
            login(request,user)
            # return redirect('/students/students/')
            
            if request.user.is_staff:
                return redirect('/students/dashboard/')
            else:
                return redirect('/students/dashboard/')
        else:
            context={
                'error':'*Invalid Username Or Password'
            }
        
    return render(request,'login.html',context)

@login_required(login_url='/')
def logoutPage(request):
    logout(request)
    return redirect('/')


def SignupPage(request):
    
    context={
        'error':""
    }
    if request.method =="POST":
        user_check=User.objects.filter(username=request.POST['username'])
        print(user_check)
        
        if len(user_check)>0:
            context={
                'error':'*user is already exits'
            }
            return render(request,'signup.html',context)
        else:
            new_user=User(username=request.POST['username'],email=request.POST['email'],
                        )
            
            new_user.set_password(request.POST['password'])
            new_user.save()
            
            return redirect('/')            
            
        
    return render(request,'signup.html',context)






