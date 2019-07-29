# Generated by Django 2.1 on 2019-07-23 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190507_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id_activity', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('state', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(choices=[('C', 'Ortopedista'), ('A', 'Analista de requerimientos'), ('I', 'Ingenieria inversa'), ('D', 'Diseñador'), ('P', 'P rapido'), ('G', 'Gestor de conocimiento'), ('M', 'Metodologia')], max_length=1)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='CasePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='case',
            old_name='fk_patient',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='fk_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='fk_package',
            new_name='package',
        ),
        migrations.RemoveField(
            model_name='case',
            name='fk_package',
        ),
        migrations.AlterField(
            model_name='case',
            name='state',
            field=models.CharField(choices=[('1', 'cotizacion'), ('2', 'ejecucion'), ('3', 'suspencion'), ('4', 'finalizacion')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('C', 'Ortopedista'), ('A', 'Analista de requerimientos'), ('I', 'Ingenieria inversa'), ('D', 'Diseñador'), ('P', 'P rapido'), ('G', 'Gestor de conocimiento'), ('M', 'Metodologia')], max_length=1),
        ),
        migrations.AddField(
            model_name='casepackage',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Case'),
        ),
        migrations.AddField(
            model_name='casepackage',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Package'),
        ),
        migrations.AddField(
            model_name='activity',
            name='case_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.CasePackage'),
        ),
        migrations.AddField(
            model_name='case',
            name='package',
            field=models.ManyToManyField(through='User.CasePackage', to='User.Package'),
        ),
        migrations.AlterUniqueTogether(
            name='assigned',
            unique_together={('user', 'activity')},
        ),
    ]
