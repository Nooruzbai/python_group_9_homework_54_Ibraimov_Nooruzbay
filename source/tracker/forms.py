from django import forms

from .models import Task, Type


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }
