# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20180408_1435'),
        ('orders', '0002_auto_20180408_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
    ]
