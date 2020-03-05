"""priya_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app1.models import Data_Saved
from app1 import views
from django.views.generic import DetailView, TemplateView, ListView, UpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    #path('search/',ListView.as_view(template_name='search.html',model=Data_Saved),name='search'),
    path('list/',ListView.as_view(template_name='showall.html',model=Data_Saved),name='list'),
    path('search/',views.save,name='search'),
    path('detail/',views.detail)
]
