from django.shortcuts import render
from TaskModel.models import TaskModel

def home(request):
    data = TaskModel.objects.all()

