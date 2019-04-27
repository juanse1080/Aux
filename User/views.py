from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

from .forms import createPatientForm, createF01Form
from .models import User, Case, Patient, Package

@login_required
def detailF01(request, pk):
    return render(request, 'user/detailF01.html', {'case': Case.objects.get(id_case=pk), 'packages' : Package.objects.all()})

@login_required    
def board(request):
    return render(request, 'user/board.html', {'case': Case.objects.all()})

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

@login_required
def createF01(request):
    if request.method == 'POST':
        request.POST._mutable = True
        if request.POST.get('screw') == 'otro':
            request.POST.update({'screw': request.POST.get('screw_t')})
        if request.POST.get('recession') == '0':
            request.POST.update({'margen_recession': None, 'fastenings' : None})   
        form = createF01Form(request.POST)
        if form.is_valid():
            form.cleaned_data
            F01 = form.save(commit=False)
            F01.fk_user = request.user
            F01.save()
            return redirect(board)
        return render(request, 'user/createPatient.html', {'errors':form.errors, 'packages' : Package.objects.all()})
    return render(request, 'user/createPatient.html', {'packages' : Package.objects.all() })

@login_required
def filterPatient(request):
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

