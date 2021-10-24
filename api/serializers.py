from rest_framework import serializers

from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'


class StepTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepType
        fields = '__all__'


class HistoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryType
        fields = '__all__'


class TravelStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelStep
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarIssue
        fields = '__all__'


class LevelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelTag
        fields = '__all__'


class UserTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTravel
        fields = '__all__'


class UserTravelStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTravelStep
        fields = '__all__'


class UserInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInsurance
        fields = '__all__'


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = '__all__'


class UserCarHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCarHistory
        fields = '__all__'
