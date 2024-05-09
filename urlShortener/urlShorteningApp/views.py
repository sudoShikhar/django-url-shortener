from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import secrets

from .forms import MakeShortForm, GetLongForm
from .models import UrlMapping


def home(request):
    return render(request, "template.html" , { 'home' : True })

def makeShort(request):
    # Using secrets.token_hex(4) for generating new hashes.
    if request.method == 'POST':
        makeForm = MakeShortForm(request.POST)
        if makeForm.is_valid():
            long_url = makeForm.cleaned_data['longUrl']
            if UrlMapping.objects.filter(longURL=long_url).exists():
                short_url = UrlMapping.objects.get(longURL=long_url).shortURL
                output_result = request.build_absolute_uri(short_url)
            else:
                short_url = secrets.token_hex(4)
                while UrlMapping.objects.filter(shortURL=short_url).exists():
                    short_url = secrets.token_hex(4)
                new_db_entry = UrlMapping(longURL=long_url, shortURL=short_url)
                new_db_entry.save()
            output_result = request.build_absolute_uri(short_url)
            return render(request, "template.html", {
                'form':MakeShortForm(request.POST),
                'output_result': output_result,
                'res_label': "Short URL"
                })
        else:
            return render(request, 'template.html', {
                'form':MakeShortForm(request.POST),
                'res_label': "Short URL",
                'output_result': 'Please verify URL...',
            })
    else:
        return render(request, 'template.html', {
            'form':MakeShortForm(),
            'res_label': "Short URL"
            })


def getLong(request):
    if request.method == 'POST':
        getForm = GetLongForm(request.POST)
        if getForm.is_valid():
            short_url = getForm.cleaned_data['shortUrl'].split(reverse('url_shortener_home'))[-1]
            if UrlMapping.objects.filter(shortURL=short_url).exists():
                output_result = UrlMapping.objects.get(shortURL=short_url).longURL
            else:
                output_result = "Short URL not found in DB. Please create new entry with `make-short-url` endpoint."
            return render(request, "template.html", {
                'form':GetLongForm(request.POST),
                'res_label': "Long URL",
                'output_result': output_result,
                })
    else:
        return render(request, 'template.html', {
            'form':GetLongForm(),
            'res_label': "Long URL"
            })

def urlRedirector(request,urlHash):
    if UrlMapping.objects.filter(shortURL=urlHash).exists():
        long_url = UrlMapping.objects.get(shortURL=urlHash).longURL
        return redirect(long_url)
    else:
        return HttpResponse(
            f"Hello. You're at the urlRedirector with hash {urlHash}."
            "<br>"
            "Unfortunately this hash was not found in our database."
            )
