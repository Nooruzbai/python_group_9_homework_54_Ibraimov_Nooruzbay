from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }
