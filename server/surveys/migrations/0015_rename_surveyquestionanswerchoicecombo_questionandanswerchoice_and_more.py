# Generated by Django 5.1.3 on 2024-11-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0014_remove_survey_question_ids'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyQuestionAnswerChoiceCombo',
            new_name='QuestionAndAnswerChoice',
        ),
        migrations.AddField(
            model_name='survey',
            name='question_answer_choice_combos_ids',
            field=models.ManyToManyField(to='surveys.questionandanswerchoice'),
        ),
    ]
