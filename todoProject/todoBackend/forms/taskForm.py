from datetime import datetime
from django import forms

from todoBackend.models import TodoList

TASK_IS_DONE = [(True, "Done!"), (False, "Not yet")]
class AddTask(forms.ModelForm):
    created_at = forms.DateInput()
    class Meta:
        model = TodoList
        exclude = ("id",  )
