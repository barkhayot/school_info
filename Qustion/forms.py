from django.forms import ModelForm
from django import forms
from .models import University

class UniversityAddForm(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'School Name',
        'type': 'text',
        'class': 'form-control',

    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Location',
        'class': 'form-control',
        'type': 'text',

    }))
    ranking = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Ranking',
        'class': 'form-control',
        'type': 'text',

    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': 'form-control',
        'type': 'text',

    }))
    website = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'Hompage URL',
        'class': 'form-control',
        'type': 'text',

    }))

    class Meta:
        model = University
        fields = ['name', 'location', 'ranking', 'description', 'website']