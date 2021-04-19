from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": "Enter Task"}))
    
    class Meta:
        model = Task
        fields = '__all__'
