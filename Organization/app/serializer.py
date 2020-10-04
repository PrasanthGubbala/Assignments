from rest_framework import serializers
from .models import Organization,Departments,Designation,Employees,Employees_Attendance_Collection
from datetime import datetime


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('id','url','company_name','city','sector','contact')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departments
        fields = ('id','url','organization','department')

class DesignationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Designation
        fields = ('id', 'url', 'department', 'designation')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'url', 'name', 'age', 'address', 'contact', 'email', 'designation','org')

class EmployeeAttendenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees_Attendance_Collection
        fields = ('id', 'url', 'employee', 'date', 'status', 'start', 'end', 'break_time')
