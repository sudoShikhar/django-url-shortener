from django.contrib import admin

# Register your models here.
from .models import UrlMapping

admin.site.register(UrlMapping)