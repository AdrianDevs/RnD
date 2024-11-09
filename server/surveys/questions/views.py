from typing import Optional
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from surveys.questions.models import Brand, Question, QuestionType, Survey
from surveys.questions.serializers import (
    BrandSerializer,
    QuestionSerializerReader,
    QuestionTypeSerializer,
    SurveyQuestionAndAnswerChoiceSerializerReader,
    SurveySerializerReader,
)


class BrandList(APIView):
    def get(self, request: Request, format: Optional[str] = None):
        brands = Brand.objects.all()
        serializer: BrandSerializer = BrandSerializer(brands, many=True)
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


class SurveyViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Survey.objects.select_related('brand_id')
    serializer_class = SurveySerializerReader

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
