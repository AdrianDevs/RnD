from typing import Optional
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from surveys.questions.models import Brand, Question, QuestionType, Survey
from surveys.questions.serializers import (
    BrandSerializer,
    QuestionSerializerReader,
    QuestionTypeSerializer,
    SurveyQuestionAndAnswerChoiceSerializerReader,
    SurveyQuestionAndAnswerChoiceSerializerWriter,
    SurveySerializerReader,
    SurveySerializerWriter,
)


class BrandList(APIView):
    def get(self, request: Request, format: Optional[str] = None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request: Request, format: Optional[str] = None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionTypesList(APIView):
    def get(self, request: Request, format: Optional[str] = None):
        question_types = QuestionType.objects.all()
        serializer = QuestionTypeSerializer(question_types, many=True)
        return Response(serializer.data)


class QuestionList(APIView):
    def get(self, request: Request, format: Optional[str] = None):
        questions = Question.objects.select_related('question_type_id').all()
        serializer = QuestionSerializerReader(questions, many=True)
        return Response(serializer.data)


class SurveyViewSet(ModelViewSet):
    queryset = Survey.objects.select_related('brand_id')
    serializer_class = SurveySerializerReader

    def create(self, request, *args, **kwargs):
        data = request.data

        # Create survey
        survery_serializer = SurveySerializerWriter(data=data)
        survery_serializer.is_valid(raise_exception=True)
        survey = survery_serializer.save()

        # Create questions and answer choices
        if "questions_and_answer_choices" in data:
          questions_and_answer_choices = data['questions_and_answer_choices']
          for question_and_answer_choice in questions_and_answer_choices:
              data = {
                  'survey_id': survey.id,
                  'question_id': question_and_answer_choice['question_id'],
                  'answer_choice_ids': question_and_answer_choice['answer_choice_ids']
              }
              question_serializer = SurveyQuestionAndAnswerChoiceSerializerWriter(data=data)
              if question_serializer.is_valid(raise_exception=True):
                  question_serializer.save()
              else:
                  return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(survery_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        item = self.get_object()
        questions_queryset = item.surveyquestionandanswerchoice_set.select_related(
            'question_id', 'survey_id'
        ).prefetch_related('answer_choice_ids')
        questions_serializer = SurveyQuestionAndAnswerChoiceSerializerReader(questions_queryset, many=True)
        questions_data = questions_serializer.data
        for question in questions_data:
            question.pop('survey_id')

        serializer = self.get_serializer(item)
        data = serializer.data
        data['questions_and_answer_choices'] = questions_data
        return Response(data)
    
    def update(self, request, pk):
        data = request.data
        survey = self.get_object()
        survey_serializer = SurveySerializerWriter(survey, data=data)
        survey_serializer.is_valid(raise_exception=True)
        survey_serializer.save()

        # Delete existing questions and answer choices
        survey.surveyquestionandanswerchoice_set.all().delete()

        # Create new questions and answer choices
        if "questions_and_answer_choices" in data:
            questions_and_answer_choices = data['questions_and_answer_choices']
            for question_and_answer_choice in questions_and_answer_choices:
                data = {
                    'survey_id': survey.id,
                    'question_id': question_and_answer_choice['question_id'],
                    'answer_choice_ids': question_and_answer_choice['answer_choice_ids']
                }
                question_serializer = SurveyQuestionAndAnswerChoiceSerializerWriter(data=data)
                if question_serializer.is_valid(raise_exception=True):
                    question_serializer.save()
                else:
                    return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(survey_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        # Delete existing questions and answer choices
        survey = self.get_object()
        survey.surveyquestionandanswerchoice_set.all().delete()

        # Delete survey
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

