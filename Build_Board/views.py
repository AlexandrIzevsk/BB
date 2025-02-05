from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView
)
from .models import *


class AdvertList(ListView):
    queryset = Advert.objects.all()
    template_name = 'adverts.html'
    context_object_name = 'adverts'
    paginate_by = 10


class OneAdvertDetail(DetailView):
    # model = Post
    queryset = Advert.objects.all()
    template_name = 'one_advert.html'
    context_object_name = 'advert'


class AdvertCreate(LoginRequiredMixin,CreateView):
    raise_exception = True
