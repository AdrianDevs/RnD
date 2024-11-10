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
        fields = ['text', 'question_type']


class QuestionSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text', 'question_type_id']


class AnswerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = ['text']


class SurveySerializerReader(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()  # type: ignore

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'brand_name']

    def get_brand_name(self, obj):
        return obj.brand_id.name


class SurveySerializerWriter(serializers.ModelSerializer):
    # questions_and_answer_choices = serializers.ListField(child=serializers.DictField())

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'brand_id', ]

    # def get_questions_and_answer_choices(self, obj):
    #     return obj.questions_and_answer_choices


class SurveyQuestionAndAnswerChoiceSerializerReader(serializers.ModelSerializer):
    question = QuestionSerializerReader(source='question_id')
    answer_choices = AnswerChoiceSerializer(source='answer_choice_ids', many=True)

    class Meta:
        model = SurveyQuestionAndAnswerChoice
        fields = ['survey_id', 'question', 'answer_choices']


class SurveyQuestionAndAnswerChoiceSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAndAnswerChoice
        fields = ['survey_id', 'question_id', 'answer_choice_ids']
