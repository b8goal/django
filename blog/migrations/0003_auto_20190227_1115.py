# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_accuracy_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='M1_Train_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('location', models.CharField(max_length=30)),
                ('triglycerides', models.FloatField(blank=True, null=True)),
                ('hdl', models.FloatField(blank=True, null=True)),
                ('ldl', models.FloatField(blank=True, null=True)),
                ('sex', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('waist', models.FloatField(blank=True, null=True)),
                ('systolic_pressure', models.FloatField(blank=True, null=True)),
                ('diastolic_pressure', models.FloatField(blank=True, null=True)),
                ('fbs', models.FloatField(blank=True, null=True)),
                ('old', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('smoke', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('alcohol_hepatitis', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Accuracy_Data',
        ),
    ]
