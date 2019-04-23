from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from User import views, models

def template(request):
    print(request.user.show())
    if request.user.is_active:
        return redirect(views.board)
    else:
        if request.method == 'POST':
            # form = login(request.POST)
            # print(form.errors.__dict__)
            # if form.is_valid():
            #     print("funciono")
            #     return auth(request)
            # print("error")
            return auth(request)
            # return render(request, 'registration/login.html', {'form': form.errors})
        return render(request, 'registration/login.html')

def auth(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    login_valid = models.User.objects.get(email=email)
    pwd_valid = check_password(password, login_valid.password)
    if login_valid and pwd_valid:
        print(request.login_valid)
        login(request, login_valid)
        return redirect(views.board)
    messages.error(request, 'Credenciales incorrectas.')
    return redirect(template)

def logout_view(request):
    request.user.is_active = False
    request.user.save()
    logout(request)
    return redirect(template)
        
