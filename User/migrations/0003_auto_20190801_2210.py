from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from User import models


from django.db import migrations


class Migration(migrations.Migration):

    def combine_names(apps, schema_editor):
        """
            This method creates seven instances of the Package class
        """
        # We can't import the Person model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        names = [
            'Planeamiento pre-quirúrgico',
            'Prototipo Pre-Quirurjico',
            'Prototipo Guía Corte',
            'Biomodelo Virtual',
            'Prototipo Post-Quirurjico',
            'Molde Obtención Injertos',
            'Diseño de Implante',
        ]

        Package = apps.get_model('User', 'Package')

        for name_ in names:
            package = Package(name=name_)
            package.save()

    dependencies = [
        ('User', '0002_auto_20190801_2208'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
