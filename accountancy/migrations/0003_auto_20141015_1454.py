# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy', '0002_account_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=128, verbose_name='book_description')),
                ('valid_from', models.DateField(verbose_name='book_valid_from')),
                ('valid_to', models.DateField(verbose_name='book_valid_to')),
                ('root', models.ForeignKey(verbose_name='book_root', to='accountancy.Account')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'book_plural',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='account',
            name='parent',
            field=models.ForeignKey(related_name=b'childs', verbose_name='cuenta padre', blank=True, to='accountancy.Account', null=True),
        ),
    ]
