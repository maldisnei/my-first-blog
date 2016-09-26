# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poste', models.TextField()),
                ('created_date', models.DateTimeField(verbose_name=datetime.datetime(2016, 9, 20, 23, 24, 1, 802026, tzinfo=utc))),
                ('published_date', models.DateTimeField()),
                ('auth', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
