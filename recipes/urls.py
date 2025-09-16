from django.urls import path
from django.http import HttpResponse
from .views import home, sobre, contato


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]
