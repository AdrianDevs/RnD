from rest_framework.test import APIClient, APITestCase

from surveys.participants.models import Location, Occupation, Participant
from surveys.participants.serializers import LocationSerializer, OccupationSerializer, ParticipantSerializer

def create_location(name: str) -> Location:
    location = {'name': name}
    serializer = LocationSerializer(data=location)
    if serializer.is_valid():
        location = serializer.save()
    elif serializer.errors:
        raise Exception(serializer.errors)
    return location # type: ignore

def create_occupation(name: str) -> Occupation:
    occupation = {'name': name}
    serializer = OccupationSerializer(data=occupation)
    if serializer.is_valid():
        occupation = serializer.save()
    elif serializer.errors:
        raise Exception(serializer.errors)
    return occupation # type: ignore

def create_participant(first_name: str, last_name: str, location_id: int, occupation_id: int, age: int) -> Participant:
    participant = {'first_name': first_name, 'last_name': last_name, 'location': location_id, 'occupation': occupation_id, 'age': age}
    serializer = ParticipantSerializer(data=participant)
    if serializer.is_valid():
        participant = serializer.save()
    elif serializer.errors:
        raise Exception(serializer.errors)
    return participant # type: ignore

class TestLocations(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/locations/'

    def test_get_empty_list(self):
        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(len(result), 0)

    def test_non_empty_list(self):
        location = {'name': 'Location 1'}
        serializer = LocationSerializer(data=location)
        if serializer.is_valid():
            serializer.save()
        elif serializer.errors:
            raise Exception(serializer.errors)

        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Location 1')

class TestOccupations(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.uri = '/occupations/'

    def test_get_empty_list(self):
        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(len(result), 0)

    def test_non_empty_list(self):
        occupation = {'name': 'Occupation 1'}
        serializer = OccupationSerializer(data=occupation)
        if serializer.is_valid():
            serializer.save()
        elif serializer.errors:
            raise Exception(serializer.errors)

        response = self.client.get(self.uri)
        result = response.json()
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Occupation 1')
