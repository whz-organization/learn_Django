# TO BE DONE BY CANDIDATE

import json
from django.views import View
from django.http import JsonResponse
from django.core import serializers
from courses.models import Course

class CourseListView(View):
    def get(self,request):
        course_all = Course.objects.all()[:10]
        json_data = serializers.serialize('json', course_all)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)