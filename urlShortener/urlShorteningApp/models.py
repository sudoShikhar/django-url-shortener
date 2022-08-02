from django.db import models

# Create your models here.

class UrlMapping(models.Model):
    longURL = models.URLField(max_length = 300)
    shortURL = models.CharField(max_length = 8)

    def __str__(self):
        return self.shortURL + " for " + self.longURL