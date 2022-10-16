from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Employees.models import Department, Employee
from Employees.serializers import DepartmentSerializer, EmployeeSerializer


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     department_data = JSONParser().parse(request)
    #     department_serializer = DepartmentSerializer(data=department_data)
    #     if department_serializer.is_valid():
    #         department_serializer.save()
    #         return JsonResponse("Success", safe = False)
    #     return JsonResponse("Failure", safe = False)
    
    # elif request.method == 'PUT':
    #     department_data = JSONParser().parse(request)
    #     department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
    #     department_serializer = DepartmentSerializer(department, data = department_data)

    #     if department_serializer.is_valid():
    #         department_serializer.save()
    #         return JsonResponse("Updated", safe = False)
    #     return JsonResponse("Failure", safe = False)

    # elif request.method == 'DELETE':
    #     department = Department.objects.get(DepartmentId=id)
    #     department.delete()
    #     return JsonResponse("Deleted", safe = False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Success", safe = False)
        return JsonResponse("Failure", safe = False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee_data,  data = employee_data)

        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated", safe = False)
        return JsonResponse("Failure", safe = False)

    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted", safe = False)