from django.db import models

# Create your models here.
class TaskCategory(models.Model):
    Category_Name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.Category_Name