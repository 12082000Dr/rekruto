from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    msg = request.GET['message']
    ne = request.GET['name']
    return HttpResponse(f'<h1>Hello, {ne}!</n1> <h2>{msg}</h2>')
def pusto(request, name='Rekruto', message='Давай дружить!'):
    return HttpResponse(f'<h1>Hello, {name}!</n1> <h2>{message}</h2>')