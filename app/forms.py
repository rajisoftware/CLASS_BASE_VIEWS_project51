from app.models import *
from django import forms
class topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
