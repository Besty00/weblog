# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('text', models.TextField(verbose_name='正文')),
                ('abstract', models.TextField(verbose_name='摘要')),
                ('pubDate', models.DateField(auto_now=True, verbose_name='发布日期')),
            ],
            options={
                'verbose_name_plural': '记 录',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
