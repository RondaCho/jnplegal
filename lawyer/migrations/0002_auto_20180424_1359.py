# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='phone',
            field=models.CharField(blank=True, help_text='전화번호를 입력해주세요.', max_length=20),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='fax',
            field=models.CharField(blank=True, help_text='팩스번호를 입력해주세요.', max_length=50),
        ),
    ]
