

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from surveys.responses.models import SurveyAnswer, SurveyResponse
from surveys.responses.serializers import SurveyAnswerSerializer, SurveyResponseSerializer


class SurveyAnswerViewSet(ModelViewSet):
    queryset = SurveyAnswer.objects.select_related("survey_id", "participant_id", "question_id", "answer_choice_id")
    serializer_class = SurveyAnswerSerializer
    

class SurveyResponseViewSet(GenericViewSet):
    queryset = (SurveyResponse.objects.select_related("survey_id", "participant_id").prefetch_related("survey_answer_ids"))
    # queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer
    print("SurveyResponseViewSet")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        print("SurveyResponseViewSet list", serializer.data)
        # return self.get_paginated_response(self.paginate_queryset(serializer.data))
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

