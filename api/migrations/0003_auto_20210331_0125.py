# Generated by Django 3.1.7 on 2021-03-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210331_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
