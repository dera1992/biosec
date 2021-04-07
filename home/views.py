from rest_framework import viewsets, generics

from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from home.models import Employee

from home.serializers import  EmployeeSerializer
from rest_framework.decorators import api_view


#Employee Class Base Viewset for create,retrieve,list and update a record
class EmployeeViewset(viewsets.ViewSet):

    def create(self,request):
        try:
            serializer=EmployeeSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Employee Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Employee Data"}
        return Response(dict_response)

    def list(self,request):
        employee=Employee.objects.filter(active=True)
        serializer=EmployeeSerializer(employee,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Employee List Data","data":serializer.data}
        return Response(response_dict)

    def retrieve(self,request,pk=None):
        queryset=Employee.objects.all()
        employee=get_object_or_404(queryset,pk=pk)
        serializer=EmployeeSerializer(employee,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})

    def update(self,request,pk=None):
        queryset=Employee.objects.all()
        employee=get_object_or_404(queryset,pk=pk)
        serializer=EmployeeSerializer(employee,data=request.data,context={"request":request})
        serializer.is_valid()
        serializer.save()
        return Response({"error":False,"message":"Data Has Been Updated"})



# Funtion base view of django restframe work for achieving a record
@api_view(['DELETE'])
def archive(request, pk=None):
    employee = Employee.objects.get(id=pk)
    employee.active = False
    employee.save()
    return Response(data='delete success')
