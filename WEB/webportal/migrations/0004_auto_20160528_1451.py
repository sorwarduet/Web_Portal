# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 14:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0003_offeredcourse_studentcourseenrollment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offeredcourse',
            old_name='courses',
            new_name='course',
        ),
    ]
