from django import forms
from verby.models import Writer


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        exclude = ('password',)
