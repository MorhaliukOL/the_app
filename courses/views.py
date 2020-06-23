from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializer


class GetStudentsList(APIView):

    def get(self, request):
        students = Students.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data)
