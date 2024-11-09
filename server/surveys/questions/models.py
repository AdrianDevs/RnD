from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    question_type_id = models.ForeignKey(QuestionType, on_delete=models.RESTRICT)

    def __str__(self):
        return self.text


class AnswerChoice(models.Model):
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text


class Survey(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    brand_id = models.ForeignKey(Brand, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class SurveyQuestionAndAnswerChoice(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.RESTRICT)
    question_id = models.ForeignKey(Question, on_delete=models.RESTRICT)
    answer_choice_ids = models.ManyToManyField(AnswerChoice)

    def __str__(self):
        return f'{self.survey_id} - {self.question_id}'
