# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(default=b'REGUL', max_length=5, verbose_name='custom_user_user_type', choices=[(b'ADMIN', 'type_Administrator'), (b'REGUL', 'type_Regular'), (b'SUPER', 'type_Supervisor'), (b'AUDIT', 'type_Auditor')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'custom_user',
                'verbose_name_plural': 'custom_user_plural',
            },
            bases=(models.Model,),
        ),
    ]
