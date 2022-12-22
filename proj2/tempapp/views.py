# from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class HomePages(TemplateView):
    template_name = 'f1.html'
