# Generated by Django 2.1.3 on 2018-12-24 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsdata',
            name='update_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
