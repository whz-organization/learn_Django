from django.urls import path
from api.views import CourseListView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course'),
]
