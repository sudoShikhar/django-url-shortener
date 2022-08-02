from django import forms


class MakeShortForm(forms.Form):
    longUrl = forms.CharField(label="Long URL")
    # shortUrl = forms.CharField(label="Short URL")

class GetLongForm(forms.Form):
    # longUrl = forms.CharField(label="Long URL")
    shortUrl = forms.CharField(label="Short URL")
