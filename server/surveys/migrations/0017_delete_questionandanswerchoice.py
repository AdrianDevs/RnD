# Generated by Django 5.1.3 on 2024-11-08 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0016_remove_survey_question_answer_choice_combos_ids'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionAndAnswerChoice',
        ),
    ]
