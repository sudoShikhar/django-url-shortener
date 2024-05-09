from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='url_shortener_home'),
    path('make-short-url', views.makeShort, name='make_short'),
    path('get-long-url', views.getLong, name='get_long'),
    path('<str:urlHash>',views.urlRedirector, name='redirect_url'),
]
