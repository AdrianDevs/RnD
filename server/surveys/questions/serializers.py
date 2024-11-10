from rest_framework import serializers

from surveys.questions.models import AnswerChoice, Brand, Question, QuestionType, Survey, SurveyQuestionAndAnswerChoice


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['name', 'description']


class QuestionSerializerReader(serializers.ModelSerializer):
    question_type = QuestionTypeSerializer(source='question_type_id')

    class Meta:
        model = Question
        fields = ['text', 'question_type_id', 'question_type']


class QuestionSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', 'question_type_id']


class AnswerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = "__all__"


class SurveySerializerReader(serializers.ModelSerializer):
    brand = BrandSerializer(source='brand_id')

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'brand']


class SurveySerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'brand_id', ]


class SurveyQuestionAndAnswerChoiceSerializerReader(serializers.ModelSerializer):
    question = QuestionSerializerReader(source='question_id')
    answer_choices = AnswerChoiceSerializer(source='answer_choice_ids', many=True)

    class Meta:
        model = SurveyQuestionAndAnswerChoice
        fields = ['survey_id', 'question_id', 'question', 'answer_choice_ids', 'answer_choices']


class SurveyQuestionAndAnswerChoiceSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAndAnswerChoice
        fields = ['survey_id', 'question_id', 'answer_choice_ids']
