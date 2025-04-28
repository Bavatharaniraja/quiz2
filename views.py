from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Attendance, PerformanceRecord
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceRecordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['department', 'is_active']
    search_fields = ['name']

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PerformanceListCreateView(generics.ListCreateAPIView):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def health_check(request):
    return Response({"status": "ok"})

