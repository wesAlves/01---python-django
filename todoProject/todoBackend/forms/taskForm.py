from django import forms

TASK_IS_DONE = [(True, "Done!"), (False, "Not yet")]
class AddTask(forms.Form):
    name = forms.CharField(label='Task Name', max_length=100)
    description = forms.CharField(label='Task Description', max_length=100)
    is_done = forms.ChoiceField(required = False, widget=forms.RadioSelect, choices=TASK_IS_DONE)