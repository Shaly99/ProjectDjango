"""moflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import LoginView
from series.views import EpisodeView
from series.views import SerieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SerieView.as_view()),
    path('episodes/<int:serie_id>', EpisodeView.as_view(), name="episodes"),
    path('login/', LoginView.as_view(), name='login')
]
