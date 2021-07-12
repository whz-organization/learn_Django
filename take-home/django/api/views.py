# TO BE DONE BY CANDIDATE

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from courses.models import Course

class CourseListView(APIView):
    def get(self,request, *args, **kwargs):
        course_all = Course.objects.all()
        serializer = CourseSerializer(course_all, many=True)
        return Response(serializer.data)
    