from rest_framework import serializers

from surveys.participants.serializers import ParticipantSerializer
from surveys.questions.serializers import AnswerChoiceSerializer, SurveySerializerReader
from surveys.responses.models import SurveyAnswer, SurveyResponse


class SurveyAnswerSerializerReader(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question_id.text')  # type: ignore
    answer = AnswerChoiceSerializer(source='answer_choice_ids', many=True, read_only=True)

    class Meta:
        model = SurveyAnswer
        fields = ['question_text', 'answer']

    def get_question_text(self, obj):
        return obj.question_id.text


class SurveyAnswerSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = '__all__'


class SurveyResponseSerializerReader(serializers.ModelSerializer):
    survey = SurveySerializerReader(source='survey_id')
    participant = ParticipantSerializer(source='participant_id')
    answers = SurveyAnswerSerializerReader(source='survey_answer_ids', many=True)

    class Meta:
        model = SurveyResponse
        fields = ['survey', 'participant', 'response_date', 'answers']


class SurveyResponseSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = '__all__'
