from django import forms
from TaskModel.models import TaskModel

class TaskModel_Form(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        
        widgets = {
            'Task_Assign_Date' : forms.DateInput(attrs={'type' : 'date'})
        }