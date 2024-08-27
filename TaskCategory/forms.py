from django import forms
from TaskCategory.models import TaskCategory

class TaskCategory_Form(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'