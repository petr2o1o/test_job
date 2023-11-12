from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<title>Hello, World!</title><h1>Hello, World!</h1>')
