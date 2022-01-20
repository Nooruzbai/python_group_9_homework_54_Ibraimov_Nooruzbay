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

    def clean_summary(self):
        if self.cleaned_data.get('summary') == 'Nooruzbay Ibraimov':
            raise ValueError(f'You cannot enter my name, my name is {self.cleaned_data.get("summary")}')
        return self.cleaned_data.get('summary')

    def clean_description(self):
        if "fuck you all" or "politics" or "no vaccine" in str(self.cleaned_data.get('description')).lower():
            raise ValueError(f'You cannot enter sensitive words into the description {self.cleaned_data.get("description")}')
        return self.cleaned_data.get('description')

