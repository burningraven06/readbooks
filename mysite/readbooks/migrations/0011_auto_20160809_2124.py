# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readbooks', '0010_auto_20160808_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='critic',
            old_name='favorite_quote',
            new_name='bio',
        ),
    ]
