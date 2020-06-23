from django.urls import path
from django.views.generic import TemplateView
from .views import GetStudentsList


urlpatterns = [
    path('students/', GetStudentsList.as_view()),
    path('', TemplateView.as_view(template_name='index.html'))
]
