# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstWebsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealprovider',
            old_name='merchant_ID',
            new_name='merchant',
        ),
    ]