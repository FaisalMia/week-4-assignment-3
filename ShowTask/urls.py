from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.show_task,name='show_task'),
]