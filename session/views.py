from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from .forms import login
from User import views, models

def template(request):
    if request.method == 'POST':
        auth(request)
    return render(request, 'registration/login.html', {'form': login})

def auth(request):
    id_card = request.POST.get('id_card')
    password = request.POST.get('password')
    login_valid = models.User.objects.get(id_card=id_card)
    print(login_valid.get_full_name())
    pwd_valid = check_password(password, login_valid.password)
    if login_valid and pwd_valid:
        try:
            user = User.objects.get(id_card=id_card)
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            # user = User(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user
    return None
    # user = authenticate(request, id_card=id_card, password=password)
    # print(user)
    # if user is not None:
    #     login(request, user)
    #     return redirect(views.board)
    # else:
    #     return redirect(template)

def logout_view(request):
    logout(request)
    return redirect(template)
        
