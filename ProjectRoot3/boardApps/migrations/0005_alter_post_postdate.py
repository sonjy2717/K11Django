# Generated by Django 4.0 on 2022-01-06 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApps', '0004_alter_post_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
