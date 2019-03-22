from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .forms import createPatientForm, createF01Form
from .models import User, Case

def detailF01(request, pk):
    return render(request, 'user/detailF01.html', {'case': Case.objects.get(id_case=pk)})
    
def board(request):
    return render(request, 'user/board.html', {'case': Case.objects.all()})

def createPatient(request):
    if request.is_ajax():
        form = createPatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return JsonResponse({'success': True, 'patient': {
                'id_user': patient.id_user,
                'id_card': patient.id_card,
                'first_name': patient.first_name,
                'last_name' : patient.last_name,
                'birth' : patient.birth
            }})
        return JsonResponse({'errors':form.errors})

def createF01(request):
    if request.method == 'POST':
        request.POST._mutable = True
        if request.POST.get('screw') == 'otro':
            request.POST.update({'screw': request.POST.get('screw_t')})
        if request.POST.get('recession') == '0':
            request.POST.update({'margen_recession': None, 'fastenings' : None})   
        form = createF01Form(request.POST)
        
        if form.is_valid():
            F01 = form.save()
            return redirect(board)
        return render(request, 'user/createPatient.html', {'errors':form.errors})
    return render(request, 'user/createPatient.html')

def filterPatient(request):
    id_card = request.POST.get('id_card')
    name = request.POST.get('name')
    patients = User.objects.filter(id_card__startswith=id_card, first_name__startswith=name, last_name__startswith=name).order_by('id_card')
    data = {
        'patients': [{
            'id_user': patient.id_user,
            'id_card': patient.id_card,
            'first_name': patient.first_name,
            'last_name' : patient.last_name,
            'birth' : patient.birth
        } for patient in patients ]
    }
    return JsonResponse(data)

