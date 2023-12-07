from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from easybuy.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered successfully! Login to continue")
            return redirect('/login')
    context={"form":form}
    
    return render(request,"auth/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            passwd=request.POST.get('password')
        
            user=authenticate(request,username=name,password=passwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect("/")
            else:
                messages.error(request,"invalid Username or Password")
                return redirect('/login')
        return render(request,"auth/login.html")
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successfully")
    return redirect('/')