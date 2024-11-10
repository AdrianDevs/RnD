from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from surveys.questions.models import AnswerChoice, Brand, Question, QuestionType, Survey, SurveyQuestionAndAnswerChoice
from surveys.questions.serializers import (
    AnswerChoiceSerializer,
    BrandSerializer,
    QuestionSerializerWriter,
    QuestionTypeSerializer,
    SurveyQuestionAndAnswerChoiceSerializerWriter,
    SurveySerializerWriter,
)
from surveys.questions.views import BrandList


def create_brand(name: str) -> Brand:
    brand = {'name': name}
    brand_serializer = BrandSerializer(data=brand)
    if brand_serializer.is_valid():
        brand = brand_serializer.save()
    else:
        raise Exception(brand_serializer.errors)
    return brand


def create_empty_survey(name: str, description: str, start_date: str, end_date: str, brand_id: int) -> Survey:
    survey = {
        'name': name,
        'description': description,
        'start_date': start_date,
        'end_date': end_date,
        'brand_id': brand_id,
    }
    survey_serializer = SurveySerializerWriter(data=survey)
    if survey_serializer.is_valid():
        survey = survey_serializer.save()
    else:
        raise Exception(survey_serializer.errors)
    return survey


def create_question_type(name: str, description: str) -> QuestionType:
    question_type = {'name': name, 'description': description}
    question_type_serializer = QuestionTypeSerializer(data=question_type)
    if question_type_serializer.is_valid():
        question_type = question_type_serializer.save()
    else:
        raise Exception(question_type_serializer.errors)
    return question_type


def create_question(text: str, question_type_id: int) -> Question:
    question = {'text': text, 'question_type_id': question_type_id}
    question_serializer = QuestionSerializerWriter(data=question)
    if question_serializer.is_valid():
        question = question_serializer.save()
    else:
        raise Exception(question_serializer.errors)
    return question


def create_answer_choice(text: str) -> AnswerChoice:
    answer_choice = {'text': text}
    answer_choice_serializer = AnswerChoiceSerializer(data=answer_choice)
    if answer_choice_serializer.is_valid():
        answer_choice = answer_choice_serializer.save()
    else:
        raise Exception(answer_choice_serializer.errors)
    return answer_choice


def add_question_to_survey(survey_id: int, question_id: int, answer_choice_ids: list[int]) -> None:
    survey_question_and_answer_choice = {
        'survey_id': survey_id,
        'question_id': question_id,
        'answer_choice_ids': answer_choice_ids,
    }
    survey_question_and_answer_choice_serializer = SurveyQuestionAndAnswerChoiceSerializerWriter(
        data=survey_question_and_answer_choice
    )
    if survey_question_and_answer_choice_serializer.is_valid():
        survey_question_and_answer_choice_serializer.save()
    else:
        raise Exception(survey_question_and_answer_choice_serializer.errors)


def create_full_survey() -> Survey:
    brand = create_brand('Brand 1')
    survey = create_empty_survey('Survey 1', 'Survey 1 Description', '2021-01-01', '2021-01-31', brand.id)  # type: ignore
    question_type_1 = create_question_type('Single Choice', 'Sing Choice Question')
    question_type_2 = create_question_type('Multiple Choice', 'Multiple Choice Question')
    question_1 = create_question('What is your favorite color?', question_type_1.id)  # type: ignore
    question_2 = create_question('What is your two least favorite colors?', question_type_2.id)  # type: ignore
    answer_choice_1 = create_answer_choice('Red')
    answer_choice_2 = create_answer_choice('Green')
    answer_choice_3 = create_answer_choice('Blue')
    answer_choice_4 = create_answer_choice('Yellow')
    answer_choice_5 = create_answer_choice('Orange')
    add_question_to_survey(survey.id, question_1.id, [answer_choice_1.id, answer_choice_2.id, answer_choice_3.id])  # type: ignore
    add_question_to_survey(survey.id, question_2.id, [answer_choice_4.id, answer_choice_5.id])  # type: ignore
    return survey


class TestBrand(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = BrandList.as_view()
        self.uri = '/brands'

    def test_post_and_list(self):
        request = self.factory.post(self.uri, {'name': 'Brand 1'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)
        )

        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Brand 1')

    def test_post_invalid_data(self):
        request = self.factory.post(self.uri, {'name': ''})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 400, 'Expected Response Code 400, received {0} instead.'.format(response.status_code)
        )

    def test_get_empty_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(response.data), 0)


class TestQuestionTypes(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/question_types'

    def test_get(self):
        question_type = {'name': 'Multiple Choice', 'description': 'Multiple Choice Question'}
        serializer = QuestionTypeSerializer(data=question_type)
        if serializer.is_valid():
            serializer.save()

        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Multiple Choice')
        self.assertEqual(result[0]['description'], 'Multiple Choice Question')


class TestQuestions(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/questions'

    def test_get(self):
        question_type = {'name': 'Multiple Choice', 'description': 'Multiple Choice Question'}
        question_type_serializer = QuestionTypeSerializer(data=question_type)
        if question_type_serializer.is_valid():
            question_type = question_type_serializer.save()
        else:
            raise Exception(question_type_serializer.errors)

        question = {'text': 'What is your favorite color?', 'question_type_id': question_type.id}  # type: ignore
        question_serializer = QuestionSerializerWriter(data=question)
        if question_serializer.is_valid():
            question_serializer.save()
        else:
            raise Exception(question_serializer.errors)

        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['text'], 'What is your favorite color?')
        self.assertEqual(result[0]['question_type']['name'], 'Multiple Choice')


class TestSurveysList(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/surveys/'

    def test_get(self):
        brand = {'name': 'Brand 1'}
        brand_serializer = BrandSerializer(data=brand)
        if brand_serializer.is_valid():
            brand = brand_serializer.save()
        else:
            raise Exception(brand_serializer.errors)

        survey = {
            'name': 'Survey 1',
            'description': 'Survey 1 Description',
            'start_date': '2021-01-01',
            'end_date': '2021-01-31',
            'brand_id': brand.id,
        }  # type: ignore
        survey_serializer = SurveySerializerWriter(data=survey)
        if survey_serializer.is_valid():
            survey = survey_serializer.save()
        else:
            raise Exception(survey_serializer.errors)

        response = self.client.get(self.uri, format='json')
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Survey 1')
        self.assertEqual(result[0]['description'], 'Survey 1 Description')
        self.assertEqual(result[0]['brand_name'], 'Brand 1')


class TestSurveyDetails(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/surveys/'

    def test_get(self):
        # Create a survey with a question and an answer choice
        brand = create_brand('Brand 1')
        survey = create_empty_survey('Survey 1', 'Survey 1 Description', '2021-01-01', '2021-01-31', brand.id)  # type: ignore
        question_type = create_question_type('Multiple Choice', 'Multiple Choice Question')
        question = create_question('What is your favorite color?', question_type.id)  # type: ignore
        answer_choice = create_answer_choice('Red')
        add_question_to_survey(survey.id, question.id, [answer_choice.id])  # type: ignore

        # Get the survey details
        response = self.client.get(f'{self.uri}{survey.id}/', format='json')  # type: ignore
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(result['name'], 'Survey 1')
        self.assertEqual(result['description'], 'Survey 1 Description')
        self.assertEqual(result['brand_name'], 'Brand 1')
        self.assertEqual(len(result['questions_and_answer_choices']), 1)

    def test_create(self):
        brand = create_brand('Brand 1')
        survey = {
            'name': 'Survey 1',
            'description': 'Survey 1 Description',
            'start_date': '2021-01-01',
            'end_date': '2021-01-31',
            'brand_id': brand.id,
        }
        response = self.client.post(self.uri, survey, format='json')
        self.assertEqual(
            response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(response.json()['name'], 'Survey 1')

    def test_create_detailed_and_update_detailed(self):
        # Create a survey with a question and an answer choice
        brand = create_brand('Brand 1')
        survey = {
            'name': 'Survey 1',
            'description': 'Survey 1 Description',
            'start_date': '2021-01-01',
            'end_date': '2021-01-31',
            'brand_id': brand.id, # type: ignore
        }
        question_type_1 = create_question_type('Single Choice', 'Single Choice Question')
        question_type_2 = create_question_type('Multiple Choice', 'Multiple Choice Question')
        question_1 = create_question('What is your favorite color?', question_type_1.id)  # type: ignore
        question_2 = create_question('What is your two favorite colors?', question_type_2.id)  # type: ignore
        answer_choice_1 = create_answer_choice('Red')
        answer_choice_2 = create_answer_choice('Green')
        answer_choice_3 = create_answer_choice('Blue')
        answer_choice_4 = create_answer_choice('Purple')
        answer_choice_5 = create_answer_choice('Yellow')

        survey['questions_and_answer_choices'] = [
            {'question_id': question_1.id, 'answer_choice_ids': [answer_choice_1.id, answer_choice_4.id]},  # type: ignore
            {'question_id': question_2.id, 'answer_choice_ids': [answer_choice_2.id, answer_choice_3.id, answer_choice_4.id, answer_choice_5.id]},  # type: ignore
        ]

        response = self.client.post(self.uri, survey, format='json')
        self.assertEqual(
            response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)
        )
        
        # Fetch the saved survey
        response_data = response.json()
        response = self.client.get(f'{self.uri}{response_data["id"]}/', format='json')
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(result['name'], 'Survey 1')
        self.assertEqual(result['description'], 'Survey 1 Description')
        self.assertEqual(result['brand_name'], 'Brand 1')
        self.assertEqual(len(result['questions_and_answer_choices']), 2)
        self.assertEqual(result['questions_and_answer_choices'][0]['question']['text'], 'What is your favorite color?')
        self.assertEqual(result['questions_and_answer_choices'][1]['question']['text'], 'What is your two favorite colors?')
        self.assertEqual(len(result['questions_and_answer_choices'][0]['answer_choices']), 2)
        self.assertEqual(result['questions_and_answer_choices'][0]['answer_choices'][0]['text'], 'Red')
        self.assertEqual(result['questions_and_answer_choices'][0]['answer_choices'][1]['text'], 'Purple')
        self.assertEqual(len(result['questions_and_answer_choices'][1]['answer_choices']), 4)
        self.assertEqual(result['questions_and_answer_choices'][1]['answer_choices'][0]['text'], 'Green')
        self.assertEqual(result['questions_and_answer_choices'][1]['answer_choices'][1]['text'], 'Blue')
        self.assertEqual(result['questions_and_answer_choices'][1]['answer_choices'][2]['text'], 'Purple')
        self.assertEqual(result['questions_and_answer_choices'][1]['answer_choices'][3]['text'], 'Yellow')

        # Update the survey
        survey['name'] = 'Survey 2'
        survey['description'] = 'Survey 2 Description'
        survey['brand_id'] = brand.id
        survey['questions_and_answer_choices'][0]['answer_choice_ids'] = [answer_choice_1.id, answer_choice_2.id]
        survey['questions_and_answer_choices'][1]['answer_choice_ids'] = [answer_choice_3.id, answer_choice_4.id]
        response = self.client.put(f'{self.uri}{response_data["id"]}/', survey, format='json')

        # Fetch the updated survey
        response_data = response.json()
        response = self.client.get(f'{self.uri}{response_data["id"]}/', format='json')
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        updated_survey = response.json()
        print(updated_survey)
        self.assertEqual(updated_survey['name'], 'Survey 2')
        self.assertEqual(updated_survey['description'], 'Survey 2 Description')
        self.assertEqual(updated_survey['brand_name'], 'Brand 1')
        self.assertEqual(len(updated_survey['questions_and_answer_choices']), 2)
        self.assertEqual(updated_survey['questions_and_answer_choices'][0]['question']['text'], 'What is your favorite color?')
        self.assertEqual(updated_survey['questions_and_answer_choices'][1]['question']['text'], 'What is your two favorite colors?')
        self.assertEqual(len(updated_survey['questions_and_answer_choices'][0]['answer_choices']), 2)
        self.assertEqual(updated_survey['questions_and_answer_choices'][0]['answer_choices'][0]['text'], 'Red')
        self.assertEqual(updated_survey['questions_and_answer_choices'][0]['answer_choices'][1]['text'], 'Green')
        self.assertEqual(len(updated_survey['questions_and_answer_choices'][1]['answer_choices']), 2)
        self.assertEqual(updated_survey['questions_and_answer_choices'][1]['answer_choices'][0]['text'], 'Blue')
        self.assertEqual(updated_survey['questions_and_answer_choices'][1]['answer_choices'][1]['text'], 'Purple')

    def test_delete(self):
        # Create a survey with a question and an answer choice
        brand = create_brand('Brand 1')
        survey = {
            'name': 'Survey 1',
            'description': 'Survey 1 Description',
            'start_date': '2021-01-01',
            'end_date': '2021-01-31',
            'brand_id': brand.id, # type: ignore
        }
        question_type_1 = create_question_type('Single Choice', 'Single Choice Question')
        question_type_2 = create_question_type('Multiple Choice', 'Multiple Choice Question')
        question_1 = create_question('What is your favorite color?', question_type_1.id)  # type: ignore
        question_2 = create_question('What is your two favorite colors?', question_type_2.id)  # type: ignore
        answer_choice_1 = create_answer_choice('Red')
        answer_choice_2 = create_answer_choice('Green')
        answer_choice_3 = create_answer_choice('Blue')
        answer_choice_4 = create_answer_choice('Purple')
        answer_choice_5 = create_answer_choice('Yellow')

        survey['questions_and_answer_choices'] = [
            {'question_id': question_1.id, 'answer_choice_ids': [answer_choice_1.id, answer_choice_4.id]},  # type: ignore
            {'question_id': question_2.id, 'answer_choice_ids': [answer_choice_2.id, answer_choice_3.id, answer_choice_4.id, answer_choice_5.id]},  # type: ignore
        ]

        response = self.client.post(self.uri, survey, format='json')
        self.assertEqual(
            response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)
        )

        # Delete the survey
        response_data = response.json()
        response = self.client.delete(f'{self.uri}{response_data["id"]}/', format='json')
        self.assertEqual(
            response.status_code, 204, 'Expected Response Code 204, received {0} instead.'.format(response.status_code)
        )

        # Fetch the deleted survey
        response = self.client.get(f'{self.uri}{response_data["id"]}/', format='json')
        self.assertEqual(
            response.status_code, 404, 'Expected Response Code 404, received {0} instead.'.format(response.status_code)
        )

        # Make sure the survey is not in the list
        response = self.client.get(self.uri, format='json')
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 0)

        # Make sure the survey is not in the database
        self.assertEqual(Survey.objects.count(), 0)

        # Make sure survey questions and answer are not in the database
        self.assertEqual(SurveyQuestionAndAnswerChoice.objects.count(), 0)

        

