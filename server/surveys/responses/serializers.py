from rest_framework import serializers

from surveys.participants.serializers import ParticipantSerializer
from surveys.questions.serializers import SurveySerializer
from surveys.responses.models import SurveyAnswer, SurveyResponse

class SurveyAnswerSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source="question_id.text") # type: ignore
    answer_choice_text = serializers.CharField(source="answer_choice_id.text") # type: ignore

    class Meta:
        model = SurveyAnswer
        fields = ["question_text", "answer_choice_text"]
    
    def get_question_text(self, obj):
        return obj.question_id.text
    
    def get_answer_choice_text(self, obj):
        return obj.answer_choice_id.text
    
class SurveyResponseSerializer(serializers.ModelSerializer):
    survey = SurveySerializer(source="survey_id")
    participant = ParticipantSerializer(source="participant_id")
    answers = SurveyAnswerSerializer(source="survey_answer_ids", many=True)

    class Meta:
        model = SurveyResponse
        fields = ["survey", "participant", "response_date", "answers"]