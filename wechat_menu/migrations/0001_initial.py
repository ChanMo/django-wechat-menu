# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-18 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('type', models.CharField(blank=True, choices=[('view', 'view menu'), ('click', 'click menu')], max_length=100, null=True, verbose_name='type')),
                ('value', models.CharField(blank=True, max_length=200, null=True, verbose_name='value')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='wechat_menu.Menu')),
            ],
            options={
                'verbose_name': 'wechat menu',
                'verbose_name_plural': 'wechat_menu',
            },
        ),
    ]
