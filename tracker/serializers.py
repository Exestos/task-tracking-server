from rest_framework import serializers

from .models import (
    WorkCategory,
    WorkType,
    TimeLine
)


class WorkCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkCategory
        fields = '__all__'


class WorkTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkType
        fields = '__all__'


class TimeLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeLine
        fields = '__all__'
