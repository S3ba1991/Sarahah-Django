# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/profiles', verbose_name='Profile picture'),
        ),
    ]
