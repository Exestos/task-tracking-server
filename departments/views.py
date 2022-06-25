from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.viewsets import ModelViewSet

from authentication.models import User
from .models import Employee, Department, Position
from .serializers import UserSerializer, EmployeeSerializer, DepartmentSerializer, PositionSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = User.objects.all()
    filter_fields = ['username', 'email']


class EmployeeModelViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Employee.objects.all()
    filter_fields = ['salary', 'position']


class DepartmentModelViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset = Department.objects.all()


class PositionModelViewSet(ModelViewSet):
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Position.objects.all()
