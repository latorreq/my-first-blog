# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='created_date',
            new_name='fechAlta',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='published_date',
            new_name='fechNac',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fecNac',
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(default='', max_length=200),
        ),
    ]
