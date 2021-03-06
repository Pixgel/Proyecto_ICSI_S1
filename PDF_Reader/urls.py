"""PDF_Reader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

##django
from os import name
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

## Mio
from PDF_tranformador import views as PDF_tranformador_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PDF_tranformador_views.main, name='archivo'),
    path('descarga', PDF_tranformador_views.download, name='descarga'),
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
