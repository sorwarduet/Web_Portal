# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0002_auto_20160527_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='offeredcourse',
            name='studentCourseEnrollment',
            field=models.ManyToManyField(to='webportal.Student'),
        ),
    ]