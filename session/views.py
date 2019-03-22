from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import login
from User import views

def template(request):
    if request.method == 'POST':
        auth(request)
    return render(request, 'registration/login.html', {'form': login})

def auth(request):
    id_card = request.POST.get('id_card')
    password = request.POST.get('password')
    user = authenticate(request, id_card=id_card, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect(views.board)
    else:
        return redirect(template)

def logout_view(request):
    logout(request)
    return redirect(template)
        
