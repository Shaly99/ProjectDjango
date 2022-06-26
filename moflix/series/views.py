from getpass import GetPassWarning
from http.client import HTTPResponse
from multiprocessing import context
from pickle import GET
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        context= {
            'items': list(range(10))
        }
        return render(request, 'index.html', context=context)