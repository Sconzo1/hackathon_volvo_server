from django.utils.decorators import method_decorator
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets

from . import serializers
from .models import *


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
class TravelView(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = serializers.TravelSerializer
class StepTypeView(viewsets.ModelViewSet):
    queryset = StepType.objects.all()
    serializer_class = serializers.StepTypeSerializer
class HistoryTypeView(viewsets.ModelViewSet):
    queryset = HistoryType.objects.all()
    serializer_class = serializers.HistoryTypeSerializer
class TravelStepView(viewsets.ModelViewSet):
    queryset = TravelStep.objects.all()
    serializer_class = serializers.TravelStepSerializer
class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
class CarIssueView(viewsets.ModelViewSet):
    queryset = CarIssue.objects.all()
    serializer_class = serializers.CarIssueSerializer
class LevelTagView(viewsets.ModelViewSet):
    queryset = LevelTag.objects.all()
    serializer_class = serializers.LevelTagSerializer
class UserTravelView(viewsets.ModelViewSet):
    queryset = UserTravel.objects.all()
    serializer_class = serializers.UserTravelSerializer
class UserTravelStepView(viewsets.ModelViewSet):
    queryset = UserTravelStep.objects.all()
    serializer_class = serializers.UserTravelStepSerializer
class UserInsuranceView(viewsets.ModelViewSet):
    queryset = UserInsurance.objects.all()
    serializer_class = serializers.UserInsuranceSerializer
class UserCarView(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = serializers.UserCarSerializer
class UserCarHistoryView(viewsets.ModelViewSet):
    queryset = UserCarHistory.objects.all()
    serializer_class = serializers.UserCarHistorySerializer
