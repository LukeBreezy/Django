from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Teste 1')


def teste_index(request):
    return render(request, 'index.html')
