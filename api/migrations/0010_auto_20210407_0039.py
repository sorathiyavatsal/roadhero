# Generated by Django 3.1.7 on 2021-04-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210407_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]
