# Generated by Django 4.0 on 2022-01-06 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApps', '0005_alter_post_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]