# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_customuser_favorite_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='oauth_secret',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='oauth_token',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
