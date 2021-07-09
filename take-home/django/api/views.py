# TO BE DONE BY CANDIDATE

from django.views import View
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CourseSerializer
from courses.models import Course


class CourseListView(View):
    @api_view(['GET',])
    def courseFetch(self,request, name):
        try:
            course_all = Course.objects.filter(name=name)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "GET":
            print(request)
            serializer = CourseSerializer(course_all, many=True)
            return Response(serializer.data)