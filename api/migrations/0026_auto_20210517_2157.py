# Generated by Django 3.1.7 on 2021-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210517_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentaccount',
            name='zip_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]