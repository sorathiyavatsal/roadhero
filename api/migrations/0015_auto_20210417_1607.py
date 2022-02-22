# Generated by Django 3.1.7 on 2021-04-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210416_2314'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='verificationcode',
            name='verificatio_id_2b0100_idx',
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='mobile',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='verificationcode',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name='verificationcode',
            index=models.Index(fields=['id', 'user', 'mobile', 'code'], name='verificatio_id_1ec3da_idx'),
        ),
    ]
