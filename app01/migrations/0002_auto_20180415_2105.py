# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=20)),
                ('avatar', models.ImageField(upload_to='app01')),
            ],
        ),
        migrations.AlterField(
            model_name='area',
            name='title',
            field=models.CharField(max_length=50, verbose_name='区域名称'),
        ),
    ]
