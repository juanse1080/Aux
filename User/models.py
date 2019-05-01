from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    id_card = models.CharField(primary_key=True, max_length=15, unique=True)
    birth = models.DateField(null=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=1)
    specialty = models.TextField()
    hability = models.TextField()
    email = models.CharField(max_length=60, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)   
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.id_card

    def show(self):
        return self.__dict__

class Patient(models.Model):
    id_card = models.CharField(max_length=15, unique=True, primary_key=True)
    birth = models.DateField()
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100, null=True)

class Package(models.Model):
    id_package = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    fk_package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class Case(models.Model):
    sex_choices = (
        ('M', 'masculino'),
        ('F', 'femenino'),
    )
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
    state_choices = (
        (1, 'cotizacion'),
        (2, 'ejecucion'),
        (3, 'suspencion'),
        (4, 'finalizacion'),
    )
    id_case = models.AutoField(primary_key=True,  help_text="ID del caso")
    start_day = models.DateField(auto_now_add=True)
    fk_patient = models.ForeignKey(Patient, null=False, blank=False, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    fk_package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
    ips = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=sex_choices)
    state = models.CharField(max_length=10, choices=state_choices)
    age = models.CharField(max_length=3)
    metallic_artifact = models.BooleanField(default=False)
    deadline = models.CharField(max_length=3)
    diagnostic = models.TextField()
    process_q = models.TextField()
    etiology = models.CharField(max_length=10, choices=etiology_choices)
    zone = models.CharField(max_length=10, choices=zone_choices)
    evolution = models.CharField(max_length=10, choices=evolution_choices)
    screw = models.CharField(max_length=6,null=True)
    recession = models.BooleanField(default=False)
    margen_recession = models.CharField(max_length=6, null=True)
    fastenings = models.CharField(max_length=2, null=True)
    incisions = models.TextField()
    observations = models.TextField()

    def __str__(self):
        return self.id_case

    def show(self):
        return self.__dict__

