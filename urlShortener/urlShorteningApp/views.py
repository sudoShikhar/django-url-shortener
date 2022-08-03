from django.shortcuts import render, redirect
from django.http import HttpResponse
import secrets

from .forms import MakeShortForm, GetLongForm
from .models import UrlMapping
# hashTable = dict()

def home(request):
    # return HttpResponse(str(hashTable.values()))
    return HttpResponse("Hello, world. You're at the urlShortener home.")

def makeShort(request):
    # Using secrets.token_hex(4) for generating new hashes.
    if request.method == 'POST':
        makeForm = MakeShortForm(request.POST)
        if makeForm.is_valid():
            long_url = makeForm.cleaned_data['longUrl']
            if UrlMapping.objects.filter(longURL=long_url).exists():
                output_result = UrlMapping.objects.get(longURL=long_url).shortURL
            else:
                short_url = secrets.token_hex(4)
                while UrlMapping.objects.filter(shortURL=short_url).exists():
                    short_url = secrets.token_hex(4)
                new_db_entry = UrlMapping(longURL=long_url, shortURL=short_url)
                new_db_entry.save()
                output_result = short_url
            return render(request, "template.html", {
                'form':MakeShortForm(request.POST),
                'output_result': output_result,
                'res_label': "Short URL:"
                })
    else:
        return render(request, 'template.html', {
            'form':MakeShortForm(),
            'res_label': "Short URL:"
            })
    # return HttpResponse("Hello, world. You're at the makeShort.")

def getLong(request):
    if request.method == 'POST':
        getForm = GetLongForm(request.POST)
        if getForm.is_valid():
            short_url = getForm.cleaned_data['shortUrl']
            if UrlMapping.objects.filter(shortURL=short_url).exists():
                output_result = UrlMapping.objects.get(shortURL=short_url).longURL
            else:
                output_result = "Short URL not found in DB. Please create new entry with makeShort endpoint."
            return render(request, "template.html", {
                'form':GetLongForm(request.POST),
                'res_label': "Long URL:",
                'output_result': output_result,               
                })
    else:
        return render(request, 'template.html', {
            'form':GetLongForm(),
            'res_label': "Long URL:"
            })
    # return HttpResponse("Hello, world. You're at the getLong.")

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
