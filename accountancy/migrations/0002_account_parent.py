# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='parent',
            field=models.ForeignKey(related_name=b'parent_account', to='accountancy.Account', null=True),
            preserve_default=True,
        ),
    ]
