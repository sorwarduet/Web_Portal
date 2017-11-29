# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0005_auto_20160528_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
