from getpass import GetPassWarning
from http.client import HTTPResponse
from multiprocessing import context
from pickle import GET
from webbrowser import get
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from series.models import Episode

from series.models import Serie

# Create your views here.
class SerieView(View):

    
    def get(self, request):
        if request.user.is_authenticated:
            context= {
                'series': list(Serie.objects.all())
            }
            return render(request, 'series.html', context=context)
        raise Http404()

class EpisodeView(View):
    def get(self, request, serie_id: int):
        context= {
            'episodes': list(Episode.objects.filter(serie_id=serie_id))
        }
        return render(request, 'episodes.html', context=context)