# Generated by Django 5.1.3 on 2024-11-08 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0020_rename_surveyquestionandanswerchoices_surveyquestionandanswerchoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyquestionandanswerchoice',
            old_name='answer_choices',
            new_name='answer_choice_ids',
        ),
        migrations.RenameField(
            model_name='surveyquestionandanswerchoice',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='surveyquestionandanswerchoice',
            old_name='survey',
            new_name='survey_id',
        ),
    ]