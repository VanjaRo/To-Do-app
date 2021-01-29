from django.urls import path
from .views import ListTasks, DetailTask

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('', ListTasks.as_view()),
]
