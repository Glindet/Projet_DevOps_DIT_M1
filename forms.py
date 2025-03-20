from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    content = forms.CharField(label ='Groupe_C_Devops', widget=forms.TextInput(attrs={'placeholder':'Ajouter une Tâche...'}))
    class Meta:
        model = Task
        fields = ['content']

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'