# TO BE DONE BY CANDIDATE

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from courses.models import Course

class CourseListView(APIView):
    def get(self,request, format=None):
        course_all = Course.objects.all()
        serializer = CourseSerializer(course_all, many=True)
        return Response(serializer.data)
    