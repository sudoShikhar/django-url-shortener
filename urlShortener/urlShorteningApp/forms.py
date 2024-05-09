from django import forms
from django.core.validators import URLValidator


class MakeShortForm(forms.Form):
    longUrl = forms.URLField(label="Long URL", validators=[URLValidator()], widget=forms.TextInput(attrs={'class': 'form-control w-75 mb-3'}))
    # shortUrl = forms.CharField(label="Short URL")


class GetLongForm(forms.Form):
    # longUrl = forms.CharField(label="Long URL")
    shortUrl = forms.CharField(label="Short URL", widget=forms.TextInput(attrs={'class': 'form-control w-75 mb-3'}))
