from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    homecontext = {'ventilador': {
                    'marca': 'LG', 
                    'tamanho': 'grande'
                    }
               }
    
    return render(request, 'recipes/pages/home.html', context=homecontext, status=200)