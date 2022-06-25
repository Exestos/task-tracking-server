from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import (
    WorkCategory,
    WorkType,
    TimeLine
)

from .serializers import (
    WorkCategorySerializer,
    WorkTypeSerializer,
    TimeLineSerializer
)


class WorkCategoryModelViewSet(ModelViewSet):
    serializer_class = WorkCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkCategory.objects.all()


class WorkTypeModelViewSet(ModelViewSet):
    serializer_class = WorkTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = WorkType.objects.all()
    filter_fields = ['category']


class TimeLineModelViewSet(ModelViewSet):
    serializer_class = TimeLineSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TimeLine.objects.all()
    filter_fields = ['employee', 'work_type']

