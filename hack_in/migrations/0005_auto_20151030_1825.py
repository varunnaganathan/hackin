# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cache_in', '0004_profile_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='solved',
            field=models.CharField(default=b'', max_length=300, blank=True),
        ),
    ]
