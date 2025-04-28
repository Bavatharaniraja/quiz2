from rest_framework import serializers
from .models import Employee, Attendance, PerformanceRecord

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class PerformanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceRecord
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    attendances = AttendanceSerializer(many=True, read_only=True)
    performances = PerformanceRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
