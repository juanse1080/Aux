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
        if request.method == 'POST':
            user = auth(request)
            if user is not None:
                login(request, user)
                return redirect(views.board)
            messages.error(request, 'Credenciales incorrectas.')
        return render(request, 'registration/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect(template)

def auth(request):
    login_valid = get_user(email=request.POST['email'])
    pwd_valid = check_password(request.POST['password'], login_valid.password if login_valid else None)
    if login_valid and pwd_valid:
        return login_valid
    return None
        
def get_user(email):
    try:
        return models.User.objects.get(email=email)
    except models.User.DoesNotExist:
        return None
