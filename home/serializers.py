from rest_framework import serializers

from home.models import Employee

#The employee serializer is done here for json generation

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
