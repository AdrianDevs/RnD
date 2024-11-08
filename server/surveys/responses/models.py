from django.db import models

from surveys.participants.models import Participant
from surveys.questions.models import AnswerChoice, Question, Survey

class SurveyAnswer(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.RESTRICT)
    participant_id = models.ForeignKey(Participant, on_delete=models.RESTRICT)
    question_id = models.ForeignKey(Question, on_delete=models.RESTRICT)
    answer_choice_id = models.ForeignKey(AnswerChoice, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f"{self.survey_id} - {self.participant_id} - {self.question_id}"

class SurveyResponse(models.Model):
    survey_id = models.ForeignKey(Survey, on_delete=models.RESTRICT)
    participant_id = models.ForeignKey(Participant, on_delete=models.RESTRICT)
    response_date = models.DateField()
    survey_answer_ids = models.ManyToManyField(SurveyAnswer)
    
    def __str__(self):
        return f"{self.survey_id} - {self.participant_id}"