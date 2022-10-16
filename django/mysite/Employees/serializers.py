from rest_framework import serializers
from Employees.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentId', 
                    'DepartmentName')
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeId', 
                    'EmployeeName', 
                    'DateOfJoining',
                    'Department',
                    )
                
