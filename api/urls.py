from django.urls import path
from . import views


urlpatterns = [
    path('todos', views.TodoCreateList.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),

]