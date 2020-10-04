from django.shortcuts import render
from app.serializer import Organization,Departments,Designation,Employees,Employees_Attendance_Collection
from app.serializer import OrganizationSerializer,DepartmentSerializer,DesignationSerializer,EmployeeSerializer,EmployeeAttendenceSerializer
from rest_framework.viewsets import ModelViewSet

class Organization(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class Department(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

class Designation(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class Employee(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAttendence(ModelViewSet):
    queryset = Employees_Attendance_Collection.objects.all()
    serializer_class = EmployeeAttendenceSerializer

