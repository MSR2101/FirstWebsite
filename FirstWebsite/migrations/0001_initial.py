# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DealProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealCategory', models.CharField(max_length=100)),
                ('dealProName', models.CharField(max_length=200)),
                ('dealProAddress', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealName', models.CharField(max_length=100)),
                ('dealSummary', models.CharField(max_length=100)),
                ('dealDesc', models.CharField(max_length=500)),
                ('dealPro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstWebsite.DealProvider')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchantFirstName', models.CharField(max_length=100)),
                ('merchantLastName', models.CharField(max_length=100)),
                ('merchantDisplayName', models.CharField(max_length=200)),
                ('merchantPhoneNum', models.IntegerField(unique=True)),
                ('merchantEmail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dealprovider',
            name='merchant_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FirstWebsite.Merchant'),
        ),
    ]
