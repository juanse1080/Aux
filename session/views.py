from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from User import views, models

def template(request):
    if request.user.is_authenticated():
        return redirect(views.board)
    else:
        print(request.POST)
        if request.method == 'POST':
            user = auth(request)
            if user is not None:
                login(request, user)
                # if request.GET['next']:
                #     return render(request, request.GET['next'])
                return redirect(views.board)
            messages.error(request, 'Credenciales incorrectas.')
        return render(request, 'registration/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect(template)

def auth(request):
    login_valid = models.User.objects.get(email=request.POST['email'])
    print(login_valid)
    pwd_valid = check_password(request.POST['password'], login_valid.password)
    if login_valid and pwd_valid:
        try:
            user = models.User.objects.get(email=request.POST['email'])
            return user
        except models.User.DoesNotExist:
            return None
    return None
        
