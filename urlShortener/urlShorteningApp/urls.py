from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='urlShortenerHome'),
    path('<str:urlHash>',views.urlRedirector, name='redirect_url'),
    path('makeShortUrl', views.makeShort, name='make_short'),
    path('getLongUrl', views.getLong, name='get_long'),
]