# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_news_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='status',
            new_name='type',
        ),
    ]
