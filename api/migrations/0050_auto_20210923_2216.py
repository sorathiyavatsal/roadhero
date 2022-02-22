# Generated by Django 3.1.7 on 2021-09-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_auto_20210923_2214'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='faq',
            name='faq_id_d8ea90_idx',
        ),
        migrations.AddField(
            model_name='faq',
            name='faq_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['id', 'question', 'answer', 'faq_type'], name='faq_id_00765e_idx'),
        ),
    ]
