# Generated by Django 5.1.3 on 2024-11-08 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0010_rename_surveyquestionanswers_surveyquestionanswerchoices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyQuestionAnswerChoices',
            new_name='SurveyQuestionAnswerChoice',
        ),
    ]
