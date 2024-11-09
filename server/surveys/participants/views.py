from rest_framework import mixins, viewsets
from surveys.participants.models import Location, Occupation
from surveys.participants.serializers import LocationSerializer, OccupationSerializer


class LocationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class OccupationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
