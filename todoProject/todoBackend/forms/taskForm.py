from django import forms

class AddTask(forms.Form):
    task_name = forms.CharField(label='Task Name', max_length=100)
    task_description = forms.CharField(label='Task Description', max_length=100)