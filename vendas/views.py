from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def pdv(request):
    return render(request, 'pdv.html')

def vendas(request):
    return render(request, 'vendas.html')



