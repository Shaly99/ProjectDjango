import django
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        user = authenticate(request, usename=request.POST['username'], password=request.POST['password'])
        print (user)
        if user is not None:
            login(request, user)
            return HttpResponse(content=b'Success')
        return HttpResponse(content=b'No se logeo')