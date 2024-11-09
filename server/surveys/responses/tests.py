from rest_framework.test import APIClient, APITestCase

from surveys.participants.tests import create_location, create_occupation, create_participant
from surveys.questions.tests import (
    create_brand,
    create_empty_survey,
    create_question,
    create_question_type,
    create_answer_choice,
    add_question_to_survey,
)


class TestSurveyAnswer(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/answers/'

    def test_get_empty_list(self):
        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 0)

    def test_non_empty_list(self):
        brand = create_brand('Brand 1')
        survey = create_empty_survey('Survey 1', 'Survey 1 Description', '2021-01-01', '2021-01-31', brand.id)  # type: ignore
        question_type = create_question_type('Single Choice', 'Sing Choice Question')
        question = create_question('What is your favorite color?', question_type.id)  # type: ignore
        answer_choice_1 = create_answer_choice('Red')
        answer_choice_2 = create_answer_choice('Green')
        answer_choice_3 = create_answer_choice('Blue')
        add_question_to_survey(survey.id, question.id, [answer_choice_1.id, answer_choice_2.id, answer_choice_3.id])  # type: ignore

        location = create_location('Location 1')
        occupation = create_occupation('Occupation 1')
        participant = create_participant('John', 'Doe', location.id, occupation.id, 25)  # type: ignore

        response = self.client.post(
            self.uri,
            {
                'survey_id': survey.id,
                'participant_id': participant.id,  # type: ignore
                'question_id': question.id,
                'answer_choice_ids': [answer_choice_1.id],
            },
            format='json',
        )  # type: ignore
        self.assertEqual(
            response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)
        )

        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['question_text'], question.text)
        self.assertEqual(result[0]['answer'][0]['text'], answer_choice_1.text)


class TestSurveyResponse(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/responses/'

    def test_get_empty_list(self):
        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 0)

    def test_create_survey_response(self):
        brand = create_brand('Brand 1')
        survey = create_empty_survey('Survey 1', 'Survey 1 Description', '2021-01-01', '2021-01-31', brand.id)  # type: ignore
        question_type_1 = create_question_type('Single Choice', 'Single Choice Question')
        question_type_2 = create_question_type('Multiple Choice', 'Multiple Choice Question')
        question_1 = create_question('What is your favorite color?', question_type_1.id)  # type: ignore
        question_2 = create_question('What is your two favorite colors?', question_type_2.id)  # type: ignore
        answer_choice_1 = create_answer_choice('Red')
        answer_choice_2 = create_answer_choice('Green')
        answer_choice_3 = create_answer_choice('Blue')
        answer_choice_4 = create_answer_choice('Purple')
        answer_choice_5 = create_answer_choice('Yellow')
        add_question_to_survey(survey.id, question_1.id, [answer_choice_1.id, answer_choice_2.id, answer_choice_3.id])  # type: ignore
        add_question_to_survey(
            survey.id, question_2.id, [answer_choice_2.id, answer_choice_3.id, answer_choice_4.id, answer_choice_5.id]
        )  # type: ignore

        participant_first_name = 'John'
        participant_last_name = 'Doe'
        participant_location = create_location('Location 1')
        participant_occupation = create_occupation('Occupation 1')
        participant_age = 25

        response_date = '2021-01-01'
        answers = [
            {'question_id': question_1.id, 'answer_choice_ids': [answer_choice_1.id]},  # type: ignore
            {'question_id': question_2.id, 'answer_choice_ids': [answer_choice_3.id, answer_choice_4.id]},
        ]  # type: ignore

        data = {
            'survey_id': survey.id,
            'first_name': participant_first_name,
            'last_name': participant_last_name,  # type: ignore
            'location_id': participant_location.id,
            'occupation_id': participant_occupation.id,  # type: ignore
            'age': participant_age,
            'response_date': response_date,
            'answers': answers,
        }
        response = self.client.post(self.uri, data, format='json')
        result = response.json()
        self.assertEqual(
            response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(result['survey_id'], survey.id)  # type: ignore

        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(
            response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['survey']['name'], survey.name)
        self.assertEqual(result[0]['participant']['first_name'], participant_first_name)
        self.assertEqual(result[0]['answers'][0]['question_text'], question_1.text)
        self.assertEqual(result[0]['answers'][0]['answer'][0]['text'], answer_choice_1.text)
        self.assertEqual(result[0]['answers'][1]['question_text'], question_2.text)
        self.assertEqual(result[0]['answers'][1]['answer'][0]['text'], answer_choice_3.text)
        self.assertEqual(result[0]['answers'][1]['answer'][1]['text'], answer_choice_4.text)
