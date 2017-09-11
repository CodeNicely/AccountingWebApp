# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-08 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0003_auto_20170908_2005'),
        ('transaction', '0017_auto_20170909_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='firm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='firm.Firm'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='voucher',
            field=models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher'),
        ),
    ]