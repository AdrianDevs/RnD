from rest_framework import serializers

from surveys.models import AnswerChoice, Brand, Question, QuestionType, Survey, SurveyQuestionAndAnswerChoice


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ["name", "description"]

class QuestionSerializer(serializers.ModelSerializer):
    question_type = QuestionTypeSerializer(source="question_type_id")

    class Meta:
        model = Question
        fields = ["text", "question_type"]


class AnswerChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = ['text']


class SurveySerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField() # type: ignore

    class Meta:
        model = Survey
        fields =  ["id", "name", "description", "start_date", "end_date", "brand_name"]

    def get_brand_name(self, obj):
        return obj.brand.name

class SurveyQuestionAndAnswerChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(source='question_id')
    answer_choices = AnswerChoiceSerializer(source='answer_choice_ids', many=True)

    class Meta:
        model = SurveyQuestionAndAnswerChoice
        fields = ['survey_id', 'question', 'answer_choices']
        

class SurveyDetailedSerializer(serializers.ModelSerializer):
    questions_and_answer_choices = SurveyQuestionAndAnswerChoiceSerializer(source='surveyquestionandanswerchoice_set', many=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'brand', 'questions_and_answer_choices']


