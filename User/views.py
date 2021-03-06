from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .middleware import admin
from django.db.models import Q
from .forms import *
from .models import *

@login_required
def comments(request):
    if request.is_ajax():
        comments_ = []

        cases = request.user.cases.all()
        if len(cases) > 0:
            for case in cases:
                for package in case.case_packages.all():
                    for case_package_activity in package.case_package_activity.all():
                        for comment in case_package_activity.comments.all().order_by('created_at', 'id_comment')[:5]:
                            if comment.state and comment.user.id_card != request.user.id_card:
                                comments_.append({
                                    'comment':comment.comment,
                                    'user':comment.user.get_short_name(),
                                    'date':comment.created_at.strftime("%d de %B de %Y")
                                })

        activitys = request.user.activitys.all()
        if len(activitys) > 0:
            for activity in activitys:
                for case_package_activity in activity.case_package_activity.all():
                    for comment in case_package_activity.comments.all().order_by('created_at', 'id_comment')[:5]:
                        if comment.state and comment.user.id_card != request.user.id_card:
                            comments_.append({
                                'comment':comment.comment,
                                'user':comment.user.get_short_name(),
                                'date':comment.created_at.strftime("%d de %B de %Y")
                            })
        return JsonResponse({'success': True, 'comments': comments_})
    return JsonResponse({'errors':'Petición no es ajax'})

@login_required
def createComment(request):
    if request.is_ajax():
        form = createCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prev = data['case_package_activity'].comments.all().order_by('-created_at')
            if len(prev) > 0:
                prev[0].state = False
                prev[0].save()
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return JsonResponse({'success': True, 'comment': {
                'comment': comment.comment,
                'date': comment.created_at.strftime("%d de %B de %Y")
            }})
        return JsonResponse({'errors':form.errors})
    return JsonResponse({'errors':'Petición no es ajax'})

@login_required
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
    if request.user.role == 'A':
        activity = case.activity.all().filter(name="Requerimiento de información").filter(state=True).order_by('assigneds__created_at')
    else:
        activity = case.activity.all().filter(name="Requerimiento de información").filter(state=True).order_by('assigneds__created_at').filter(assigneds__user=request.user)
    # for i in activity:
    #     for j in i.case_package_activity.all():
    #         print(j.activity.name.encode('utf-8'))
    return render(request, 'user/detailF01.html', {
        'act' : activity,
        'case': case.case,
        'pack': case.package,
        'packages' : Package.objects.all(),
        'roles':roles
    })

@user_passes_test(admin) # using middleware admin
def requeriments(request, case, package):
    """
        This view creates information request
        Returns:
            {json}
                This is the information shown in the template
    """
    if request.is_ajax():
        form = createRequeriments(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            activity = Activity.objects.create(
                name = 'Requerimiento de información',
                description = data['comment'],
                state = True,
            )
            case_package_activity = CasePackageActivity.objects.create(
                case_package = CasePackage.objects.get(case=case, package=package),
                activity = activity
            )
            assigned = Assigned.objects.create(
                user = data['user'],
                activity = activity,
                role = data['role'],
            )
            return JsonResponse({'success': True, 'activity': {
                'id': activity.id_activity,
                'case_package': case_package_activity.id,
                'role': assigned.get_role_display(),
                'user': assigned.user.get_full_name(),
                'user_id': assigned.user.id_card,
                'description' : data['comment'],
                'date' : assigned.created_at.strftime("%d de %B de %Y")
            }})
        return JsonResponse({'errors': form.errors})
    return JsonResponse({'errors':'Petición no es ajax'})



@login_required    
def board(request):
    if request.user.role == 'C':
        req = Case.objects.filter(user=request.user).filter(state='1')
        case = Activity.objects.filter(assigneds__user=request.user).filter(state='1')
        # case = Case.objects.all()
        # print(case.package.all())
    elif request.user.role == 'A':
        case = Activity.objects.filter(state='1')
        # for i in case:
        #     for j in i.case_package.all():
        #         print(type(j))
        req = Case.objects.filter(state='1')
        # for i in case:
        #     print(i.user.first_name)
    elif request.user.role == 'I':
        req = Case.objects.filter(user=request.user).filter(state='1')
        case = Activity.objects.filter(assigneds__user=request.user).filter(state='1')
    elif request.user.role == 'D':
        req = Case.objects.filter(user=request.user).filter(state='1')
        case = Activity.objects.filter(assigneds__user=request.user).filter(state='1')
    elif request.user.role == 'P':
        req = Case.objects.filter(user=request.user).filter(state='1')
        case = Activity.objects.filter(assigneds__user=request.user).filter(state='1')
    elif request.user.role == 'G':
        req = Case.objects.filter(user=request.user).filter(state='1')
        case = Activity.objects.filter(assigneds__user=request.user).filter(state='1')
    elif request.user.role == 'M':
        req = Case.objects.filter(user=request.user).filter(state='1')
        case = Activity.objects.filter(assigneds__user=request.user).filter(state='1')
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
    """
        This view creates patients
        Returns:
            {json}
                This is a patient in json format
    """
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
    return JsonResponse({'errors':'Petición no es ajax'})
    

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
    """
        This view filters patients by id_card and full name
        Returns:
            {json}
                This is a list of patient filtered in json format
    """
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
    """
        This view filters users by role, excluding the logged in user
        Returns:
            {json}
                This is a list of users filtered in json format
    """
    if request.is_ajax():
        role = request.POST.get('role')
        users = User.objects.filter(role=role).exclude(id_card=request.user.id_card)
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
    """
        This View renders the user data that logged in
        Returns:
            {User} -- user
                This is user that logged in
    """
    return render(request, 'user/detailUser.html', {'user': User.objects.get(id_card=request.user.id_card)})

