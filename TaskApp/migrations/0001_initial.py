# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=20)),
                ('task_desc', models.TextField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/')),
                ('doc', models.FileField(default='Doc/None/No-doc.pdf', upload_to='Doc/')),
            ],
        ),
    ]
