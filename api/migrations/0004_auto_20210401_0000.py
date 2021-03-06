# Generated by Django 3.1.7 on 2021-03-31 18:30

import api.utils.common
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210331_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='service_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vehiclecompany',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=api.utils.common.path_and_rename),
        ),
    ]
