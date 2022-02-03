import re
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.contrib.auth.models import User, Group
# from rest_framework.serializers import Serializer
from itistudent.models import  students
from quickstart.serializer import Userserializer
from quickstart import serializer
from rest_framework import permissions,viewsets,status
# from crudstudent.quickstart import serializer


####################
class UserViewSet(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = Userserializer
    permission_classes = [permissions.IsAuthenticated]
# @api_view()
# def firstapi(request):
#     stud = students.objects.all()
#     serialize = Userserializer(stud,many=True)
#     return Response(serialize.data)

@api_view(['PUT', 'DELETE'])
def student_details(request, id):
    try:
        student = students.objects.get(pk=id)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'PUT':
        serializer = Userserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


