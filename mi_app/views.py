from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    context = {'mensaje': 'Hola, Django!'}
    return render(request, 'mi_app/index.html', context)