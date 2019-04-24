from django import forms
from .models import User, Case, Patient

class createPatientForm(forms.ModelForm):
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
            'fk_user',
            # 'metallic_artifacts',
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