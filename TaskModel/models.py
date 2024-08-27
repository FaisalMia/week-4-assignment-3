from django.db import models
from TaskCategory.models import TaskCategory

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=250)
    taskDescription = models.TextField()
    Task_Assign_Date = models.DateField()
    category = models.ManyToManyField(TaskCategory)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.taskTitle
