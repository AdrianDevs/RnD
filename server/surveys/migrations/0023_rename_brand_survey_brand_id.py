# Generated by Django 5.1.3 on 2024-11-09 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0022_surveyanswer_surveyresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='brand',
            new_name='brand_id',
        ),
    ]
