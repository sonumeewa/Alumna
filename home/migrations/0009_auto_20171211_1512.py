# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_friend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='user',
            new_name='users',
        ),
    ]
