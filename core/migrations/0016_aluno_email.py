# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-30 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20171130_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='E-mail'),
        ),
    ]
