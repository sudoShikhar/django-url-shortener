from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the urlShortener home.")
    
def makeShort(request):
    return HttpResponse("Hello, world. You're at the makeShort.")

def getLong(request):
    return HttpResponse("Hello, world. You're at the getLong.")

def urlRedirector(request,urlHash):
    return HttpResponse(f"Hello, world. You're at the urlRedirector with hash {urlHash}.")
