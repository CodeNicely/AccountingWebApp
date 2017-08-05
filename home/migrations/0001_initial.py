# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('mobile_no', models.CharField(max_length=10)),
                ('pan_no', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Supplier', 'Supplier'), ('Customer', 'Customer'), ('Employee', 'Employee')], default='Supplier', max_length=50)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]