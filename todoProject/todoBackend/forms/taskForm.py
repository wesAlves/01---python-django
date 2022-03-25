from datetime import datetime
from email.policy import default
from django import forms

from todoBackend.models import TodoList

TASK_IS_DONE = [(True, "Done!"), (False, "Not yet")]
class AddTask(forms.ModelForm):
    created_at = forms.DateInput()
    is_done = forms.ChoiceField(widget=forms.RadioSelect, choices=TASK_IS_DONE)
    class Meta:
        model = TodoList
        exclude = ("id",  )
