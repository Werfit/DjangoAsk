from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    text = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Ask something interesting'
    }))

    class Meta:
        model = Question
        fields = ('text', 'is_anonymous')


class SearchForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
