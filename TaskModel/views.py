from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def add_model(request):
    if request.method == 'POST':
        model_form = forms.TaskModel_Form(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect("add_model")
    else:
        model_form = forms.TaskModel_Form()
    return render(request,'add_model.html',{'form' : model_form})

def edit_model(request,id):
    model = models.TaskModel.objects.get(pk=id)
    model_form = forms.TaskModel_Form(instance=model)
    
    if request.method == 'POST':
        model_form = forms.TaskModel_Form(request.POST,instance=model)
        if model_form.is_valid():
            model_form.save()
            return redirect("show_task")
    return render(request,'add_model.html',{'form' : model_form})

def delete_model(request,id):
    model = models.TaskModel.objects.get(pk=id)
    model.category.clear()
    model.delete()
    return redirect("show_task")