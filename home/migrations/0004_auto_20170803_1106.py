# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-03 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_ledger_firm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='firm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firm.Firm'),
        ),
    ]
