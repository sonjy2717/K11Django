# Generated by Django 4.0 on 2022-01-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApps', '0003_alter_post_postdate_alter_post_visitcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
