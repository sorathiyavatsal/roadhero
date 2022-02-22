# Generated by Django 3.1.7 on 2021-05-17 16:42

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20210517_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentaccount',
            name='back_image',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='paymentaccount',
            name='front_image',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='image1',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='image2',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='image3',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='image4',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
    ]