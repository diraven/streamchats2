# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150107_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
