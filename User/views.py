from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .middleware import admin
from django.db.models import Q
from .forms import createPatientForm, createF01Form
from .models import User, Case, Patient, Package, CasePackage

@user_passes_test(admin)
def detailF01(request, case, package):
    roles = {
        'C':'Ortopedista',
        'A':'Analista de requerimientos',
        'I':'Ingenieria inversa',
        'D':'Diseñador',
        'P':'P rapido',
        'G':'Gestor de conocimiento',
        'M':'Metodologia',
    }
    case = CasePackage.objects.get(case=case, package=package)
    return render(request, 'user/detailF01.html', {
        'case': case.case,
        'pack': case.package,
        'packages' : Package.objects.all(),
        'roles':roles
    })

@login_required    
def board(request):
    if request.user.role == 'C':
        req = Case.objects.all()
        case = Case.objects.filter(user=request.user.id_card)
        # case = Case.objects.all()
        # print(case.package.all())
    elif request.user.role == 'A':
        req = Case.objects.filter(state='1')
        case = None
    elif request.user.role == 'I':
        req = None
        case = None
    elif request.user.role == 'D':
        req = None
        case = None
    elif request.user.role == 'P':
        req = None
        case = None
    elif request.user.role == 'G':
        req = None
        case = None
    elif request.user.role == 'M':
        req = None
        case = None
    else:
        pass
    return render(
        request, 
        'user/board.html', 
        {
            'case': case,
            'req': req,
        }
    )

@login_required
def createPatient(request):
    if request.is_ajax():
        form = createPatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return JsonResponse({'success': True, 'patient': {
                'id_card': patient.id_card,
                'first_name': patient.first_name,
                'last_name' : patient.last_name,
                'birth' : patient.birth
            }})
        return JsonResponse({'errors':form.errors})
    return JsonResponse({'errors':'peticion no es ajax'})
    

@login_required
def createF01(request):
    if request.method == 'POST':
        request.POST._mutable = True
        if request.POST.get('screw') == 'otro':
            request.POST.update({'screw': request.POST.get('screw_t')})
        if request.POST.get('recession') == '0':
            request.POST.update({'margen_recession': None, 'fastenings' : None})   
        form = createF01Form(request.POST)
        if form.is_valid(): #data valid, save form
            data = form.cleaned_data
            F01 = form.save(commit=False)
            F01.user = request.user
            F01.save()
            CasePackage.objects.create(
                case=F01,
                package=data['package']
            )
            return redirect(board)
        data = form.cleaned_data
        if "patient" in data:
            data['cedula'] = data['patient'].id_card
            data['name'] = data['patient'].get_full_name()
        return render(request, 'user/createPatient.html', {'errors':form.errors, 'packages' : Package.objects.all(), 'data': data})
    return render(request, 'user/createPatient.html', {'packages' : Package.objects.all() })

@login_required
def filterPatient(request):
    if request.is_ajax():
        id_card = request.POST.get('id_card')
        name = request.POST.get('name')
        patients = Patient.objects.filter(Q(id_card__contains=id_card) | Q(first_name__contains=name) | Q(last_name__contains=name))
        data = {
            'patients': [{
                'id_card': patient.id_card,
                'first_name': patient.first_name,
                'last_name' : patient.last_name,
                'birth' : patient.birth
            } for patient in patients ]
        }
        return JsonResponse(data)
    return None

@login_required
def filterRole(request):
    if request.is_ajax():
        role = request.POST.get('role')
        users = User.objects.filter(role=role)
        data = {
            'users': [{
                'id_card': user.id_card,
                'name': user.get_full_name(),
            } for user in users ]
        }
        return JsonResponse(data)
    return None


@login_required
def detailUser(request):
    print(User.objects.get(id_card=request.user.id_card).show())
    return render(request, 'user/detailUser.html', {'user': User.objects.get(id_card=request.user.id_card)})

