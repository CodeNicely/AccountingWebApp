# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-08 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170908_2005'),
        ('transaction', '0015_auto_20170820_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], default='Debit', max_length=50)),
                ('description', models.CharField(default='No description', max_length=500)),
                ('mode', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank')], default='Cash', max_length=50)),
                ('amount', models.FloatField(default=0.0)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ledger')),
                ('voucher', models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Voucher')),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='ledger',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='voucher',
        ),
        migrations.RemoveField(
            model_name='impress',
            name='ledger',
        ),
        migrations.RemoveField(
            model_name='impress',
            name='voucher',
        ),
        migrations.RemoveField(
            model_name='receive',
            name='ledger',
        ),
        migrations.RemoveField(
            model_name='receive',
            name='voucher',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Impress',
        ),
        migrations.DeleteModel(
            name='Receive',
        ),
    ]