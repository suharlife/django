# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='firstname',
            field=models.CharField(default=b'firstname', max_length=20),
        ),
    ]
