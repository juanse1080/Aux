from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from User import models


from django.db import migrations


def combine_names(apps, schema_editor):
    esp = models.User(
        email = 'especialista@gmail.com', 
        password = make_password('clave'),
        is_superuser = True,
        is_staff = True,
        is_active = True,
        id_card = 1,
        birth = '1997-09-14',
        first_name = 'Especialista',
        last_name = 'Ortopedista',
        phone = '3154390477',
        address = 'cra 19#3-82 apt 102',
        role = 'C',
        specialty = '',
        hability = ''
    )
    esp.save()
    ing = models.User(
        email = 'ingenieria@gmail.com', 
        password = make_password('clave'),
        is_superuser = False,
        is_staff = True,
        is_active = True,
        id_card = 2,
        birth = '1997-09-14',
        first_name = 'Ingenieria',
        last_name = ' Inversa',
        phone = '3154390477',
        address = 'cra 19#3-82 apt 102',
        role = 'I',
        specialty = '',
        hability = ''
    )
    ing.save()
    ana = models.User(
        email = 'analista@gmail.com', 
        password = make_password('clave'),
        is_superuser = False,
        is_staff = True,
        is_active = True,
        id_card = 3,
        birth = '1997-09-14',
        first_name = 'Analista',
        last_name = 'Requerimientos',
        phone = '3154390477',
        address = 'cra 19#3-82 apt 102',
        role = 'A',
        specialty = '',
        hability = ''
    )
    ana.save()
class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(combine_names),
    ]
