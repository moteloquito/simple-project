# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=128, verbose_name='descripci\xf3n')),
                ('account_type', models.CharField(max_length=4, verbose_name='tipo de cuenta', choices=[(b'ROOT', 'ra\xedz'), (b'ASSE', 'activos'), (b'LIAB', 'pasivos'), (b'OBLI', 'obligaciones')])),
            ],
            options={
                'verbose_name': 'cuenta',
                'verbose_name_plural': 'cuentas',
            },
            bases=(models.Model,),
        ),
    ]
