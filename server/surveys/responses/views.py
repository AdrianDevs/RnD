

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from surveys.participants.serializers import ParticipantSerializer
from surveys.responses.models import SurveyAnswer, SurveyResponse
from surveys.responses.serializers import SurveyAnswerSerializerReader, SurveyAnswerSerializerWriter, SurveyResponseSerializerReader, SurveyResponseSerializerWriter


class SurveyAnswerViewSet(ModelViewSet):
    queryset = SurveyAnswer.objects.select_related("survey_id", "participant_id", "question_id").prefetch_related("answer_choice_ids")
    serializer_class = SurveyAnswerSerializerReader

    def create(self, request, *args, **kwargs):
        serializer = SurveyAnswerSerializerWriter(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class SurveyResponseViewSet(GenericViewSet):
    queryset = (SurveyResponse.objects.select_related("survey_id", "participant_id").prefetch_related("survey_answer_ids"))
    serializer_class = SurveyResponseSerializerReader

    def create(self, request, *args, **kwargs):
        data = request.data

        survey_id = data['survey_id']
        response_date = data['response_date']

        # Create participant
        first_name = data['first_name']
        last_name = data['last_name']
        location_id = data['location_id']
        occupation_id = data['occupation_id']
        age = data['age']

        participant = {'first_name': first_name, 'last_name': last_name, 'location': location_id, 'occupation': occupation_id, 'age': age}
        serializer = ParticipantSerializer(data=participant)
        if serializer.is_valid():
            participant = serializer.save()
        elif serializer.errors:
            raise Exception(serializer.errors)
        
        # Create answers
        answers = data['answers']
        answer_ids = []
        for answer in answers:
            question_id = answer['question_id']
            answer_choice_ids = answer['answer_choice_ids']
            survey_answer = {'survey_id': survey_id, 'participant_id': participant.id, 'question_id': question_id, 'answer_choice_ids': answer_choice_ids}
            serializer = SurveyAnswerSerializerWriter(data=survey_answer)
            if serializer.is_valid():
                save_answer = serializer.save()
                answer_ids.append(save_answer.id)
            elif serializer.errors:
                raise Exception(serializer.errors)
            
        survey_response = {'survey_id': survey_id, 'participant_id': participant.id, 'response_date': response_date, 'survey_answer_ids': answer_ids}

        serializer = SurveyResponseSerializerWriter(data=survey_response)
        if serializer.is_valid():
            serializer.save()
        elif serializer.errors:
            raise Exception(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def destroy(self, request):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

