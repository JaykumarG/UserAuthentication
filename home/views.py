from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
#userid and password for test is user = jaykumar password = Soumya@123#


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,'index.html')

def loginuser(request):

    if request.method=="POST":
        username= request.POST.get("userkaname")
        password= request.POST.get("password")
        # print(username, password)

        #Check if user is entered correct credentials
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)          
            # A backend authenticated the credentials
            # print(user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')


    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    # Redirect to a success page.
    # return render(request,'login.html')
    return redirect("/login")
