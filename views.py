from django.shortcuts import redirect, render
from registration.models import Register
from .forms import RegisterForm, SignUpForm
from .models import Register, SignUp

def registration_form(request,id=0):
    if request.method =="GET":
        if id==0:
            form = RegisterForm()
        else:
            register =Register.objects.get(pk=id)
            form= RegisterForm(instance=register)
        return render(request, 'registration/registration_form.html', {'form':form})
    else:
        if id==0:
            form =  RegisterForm(request.POST)
        else:
            register =Register.objects.get(pk=id)
            form = RegisterForm(request.POST,register, instance=register)
        if form.is_valid():
            form.save()
        return redirect('register/list/')


def registration_list(request):
    context = {'register_list':Register.objects.all()}
    return render(request, 'registration/register_list.html', context)

def registration_delete(request):
    return

def signup(request):
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})