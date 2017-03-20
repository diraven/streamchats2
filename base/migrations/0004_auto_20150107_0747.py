# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.TextField(default='Title', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.TextField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.TextField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=tinymce.models.HTMLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='text_en',
            field=tinymce.models.HTMLField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='text_ru',
            field=tinymce.models.HTMLField(null=True),
            preserve_default=True,
        ),
    ]
