# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(default=b'REGUL', max_length=5, verbose_name='tipo de usuario', choices=[(b'ADMIN', 'administrador'), (b'REGUL', 'normal'), (b'SUPER', 'supervisor'), (b'AUDIT', 'auditor')]),
        ),
    ]
