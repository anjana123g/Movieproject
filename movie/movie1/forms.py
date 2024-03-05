from django import forms
from movie1.models import Movie
class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"