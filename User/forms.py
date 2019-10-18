from django import forms
from .models import *

class createCommentForm(forms.ModelForm):
    """
        Comment creation form
        Attributes:
            comment {str}
                This attribute is the comment
            case_package_activity {CasePackageActivity}
                This attribute is the model of the relationship between the case, the package and the activity
    """
    comment = forms.CharField()
    case_package_activity = forms.ModelChoiceField(queryset=CasePackageActivity.objects.all(), empty_label=None)
    class Meta:
        model = Comment
        fields = [
            'comment', 
            'case_package_activity',
        ]

class createPatientForm(forms.ModelForm):
    """
        Patient creation form
        Attributes:
            id_card {str}
                This attribute is patient identification
            birt {date}
                This attribute is the patient's date of birth
            first_name {str}
                This attribute is the patient's first name
            last_name {str}
                This attribute is the patient's last name
            phone {int}
                This attribute is the patient's phone number
            address {str}
                This attribute is the patient's address

    """
    id_card = forms.CharField(max_length=15)
    birth = forms.DateField(input_formats=["%m/%d/%Y"])
    first_name = forms.CharField(max_length=35)
    last_name = forms.CharField(max_length=35)
    phone = forms.IntegerField(max_value=9999999999)
    address = forms.CharField(max_length=100)
    class Meta:
        model = Patient
        fields = [
            'id_card', 
            'birth', 
            'first_name', 
            'last_name',
            'phone',
            'address',
        ]
    
class createRequeriments(forms.ModelForm):
    """
        Requeriments creation form
        Attributes:
            user {User}
                This attribute is the selected user
            role {str:role_choices}
                This attribute is the selected position
            comment {str}
                This attribute is the comment corresponding to the requirement
    """
    role_choices = (
        ('C', 'Ortopedista'),
        ('A', 'Analista de requerimientos'),
        ('I', 'Ingenieria inversa'),
        ('D', 'Diseñador'),
        ('P', 'P rapido'),
        ('G', 'Gestor de conocimiento'),
        ('M', 'Metodologia'),
    )
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    role = forms.ChoiceField(choices=role_choices)
    comment = forms.CharField()
    class Meta:
        model = Assigned
        fields = [
            'user',
            'role',
            'comment'
        ]


class createF01Form(forms.ModelForm):
    
    etiology_choices = (
        ('c', 'congenito'),
        ('o', 'oncologico'),
        ('t', 'traumatico'),
    )
    zone_choices = (
        ('s', 'superior'),
        ('m', 'media'),
        ('i', 'inferior'),
        ('c', 'craneo'),
    )
    evolution_choices = (
        ('a', 'agudo'),
        ('s', 'subagudo'),
        ('c', 'cronico'),
    )
    """
        Form F01 corresponds to the request
        Attributes:
            patient {Patient}
                This attribute is the selected patient
            package {str}
                This attribute is the selected package
            process_q {str}
                This attribute is the surgical process
            etiology {str:etiology_choices}
                This attribute is the selected etiology
            zone {str:zone_choices}
                This attribute is the selected zone
            evolution {str:evolution_choices}
                This attribute is the selected evolution
            screw {str}
                This attribute is the screw thickness
            recession {str}
                This attribute is the status of the recession
            margen_recession {str}
                This attribute is the margen of recession
            fastenings {str}
                --
            incisions {str}
                This attribute is the description of the planned incisions
            observations {str}
                This attribute is the observations
    """
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label=None)
    package = forms.ModelChoiceField(queryset=Package.objects.all(), empty_label=None)
    process_q = forms.CharField()
    etiology = forms.ChoiceField(choices=etiology_choices)
    zone = forms.ChoiceField(choices=zone_choices)
    evolution = forms.ChoiceField(choices=evolution_choices)
    screw = forms.CharField()
    recession = forms.BooleanField()
    margen_recession = forms.CharField(required=False)
    fastenings = forms.CharField(required=False)
    incisions = forms.CharField()
    observations = forms.CharField()
    class Meta:
        model = Case
        fields = [
            'package',
            'patient',
            'process_q',
            'etiology',
            'zone',
            'evolution',
            'screw',
            'recession',
            'margen_recession',
            'fastenings',
            'incisions',
            'observations',
        ]