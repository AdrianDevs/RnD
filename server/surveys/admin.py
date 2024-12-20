from django.contrib import admin

from surveys.participants.models import Location, Occupation, Participant
from surveys.questions.models import AnswerChoice, Brand, Question, QuestionType, Survey, SurveyQuestionAndAnswerChoice
from surveys.responses.models import SurveyAnswer, SurveyResponse

admin.site.register(Brand)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(AnswerChoice)
admin.site.register(Survey)
admin.site.register(SurveyQuestionAndAnswerChoice)
admin.site.register(Location)
admin.site.register(Occupation)
admin.site.register(Participant)
admin.site.register(SurveyAnswer)
admin.site.register(SurveyResponse)
