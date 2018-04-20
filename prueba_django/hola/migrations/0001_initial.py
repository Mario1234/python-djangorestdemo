# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('dni_sin_letra', models.IntegerField(default=12345678)),
                ('sexo', models.CharField(choices=[(b'Hombre', b'Hombre'), (b'Mujer', b'Mujer')], max_length=10)),
            ],
        ),
    ]
