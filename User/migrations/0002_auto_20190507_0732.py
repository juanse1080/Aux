from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password


from django.db import migrations


def combine_names(apps, schema_editor):
    User = apps.get_model('User', 'User')
    admin = User(
        email = 'juanmarcon1080@gmail.com', 
        password = make_password('clave'),
        is_superuser = True,
        is_staff = True,
        is_active = True,
        id_card = 1102384370,
        birth = '1997-09-14',
        first_name = 'Juan Sebastian',
        last_name = 'Marcon Caballero',
        phone = '3154390477',
        address = 'cra 19#3-82 apt 102',
        role = 1,
        specialty = '',
        hability = ''
    )
    admin.save()
    ing = User(
        email = 'juanmarcon@gmail.com', 
        password = make_password('clave'),
        is_superuser = False,
        is_staff = True,
        is_active = True,
        id_card = 1102384370,
        birth = '1997-09-14',
        first_name = 'Ingenieria Inversa',
        last_name = 'Marcon Caballero',
        phone = '3154390477',
        address = 'cra 19#3-82 apt 102',
        role = 1,
        specialty = '',
        hability = ''
    )
    ing.save()
class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(combine_names),
    ]
