# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
