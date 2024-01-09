from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'Hello, Django World!',
        'numbers': [1, 2, 3, 4, 5]
    }

    return render(request, 'base.html', context)