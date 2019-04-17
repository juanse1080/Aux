from django.db import models

class User(models.Model):

    REQUIRED_FIELDS = ('password')
    USERNAME_FIELD = ('id_card')
    is_anonymous = True
    is_authenticated = False
    id_user = models.AutoField(primary_key=True)
    id_card = models.CharField(max_length=15)
    birth = models.DateField()
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=1)
    password = models.CharField(max_length=20)
    specialty = models.TextField()
    hability = models.TextField()
    email = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.id_user

    def show(self):
        return self.__dict__

class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    id_card = models.CharField(max_length=15)
    birth = models.DateField()
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

class Package(models.Model):
    id_package = models.AutoField(primary_key=True)

class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    fk_package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)


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
    id_case = models.AutoField(primary_key=True,  help_text="ID del caso")
    start_day = models.DateField(auto_now_add=True)
    fk_patient = models.ForeignKey(Patient, null=False, blank=False, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    fk_package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
    ips = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=sex_choices)
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

