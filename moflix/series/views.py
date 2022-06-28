from getpass import GetPassWarning
from http.client import HTTPResponse
from multiprocessing import context
from pickle import GET
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from series.models import Serie

# Create your views here.
class SerieView(View):
    def get(self, request):
        context= {
            'series': list(Serie.objects.all)
        }
        return render(request, 'series.html', context=context)