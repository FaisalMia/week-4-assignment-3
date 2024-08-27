from django.shortcuts import render
from TaskModel.models import TaskModel

# Create your views here.
def show_task(request):
    data = TaskModel.objects.all()
    return render(request,'show.html',{'data' : data})