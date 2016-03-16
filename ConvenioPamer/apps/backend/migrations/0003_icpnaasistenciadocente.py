# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_acadofertaacademica_horarioturnohoras_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='icpnaAsistenciaDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingreso_fecha', models.DateField(auto_now=True)),
                ('ingreso_hora', models.TimeField(auto_now=True)),
                ('salida_fecha', models.DateField(auto_now=True)),
                ('salida_hora', models.TimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.TextField(blank=True, null=True)),
                ('workstation_ip', models.TextField(blank=True, null=True)),
                ('docente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.icpnaDocente')),
                ('ofertaacademica_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.acadOfertaAcademica')),
            ],
        ),
    ]
