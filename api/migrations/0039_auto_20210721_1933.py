# Generated by Django 3.1.7 on 2021-07-21 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20210721_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venderdetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_details', to='api.user', unique=True),
        ),
    ]
