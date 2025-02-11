from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from .forms import PostForm, FeedbackForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
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
    model = Advert
    form_class = PostForm
    template_name = 'advert_edit.html'

    def form_valid(self, form):
        advert = form.save(commit=False)
        user = self.request.user
        customer = Customer.objects.create(user=user)
        advert.author = customer
        return super().form_valid(form)

class AdvertUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('Build_Board.change_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Advert
    # и новый шаблон, в котором используется форма.
    template_name = 'advert_update.html'

    def get(self, *args, **kwargs):
        id = kwargs.get('pk')
        item = Advert.objects.get(pk=id)
        if self.request.user == item.user:
            return item


    def form_valid(self, form):
        news = form.save(commit=False)
        news.choice = 'NS'
        return super().form_valid(form)


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_edit.html'


class FeedbackCustomer(ListView):

    template_name = 'feedback.html'
    context_object_name = 'feedbacks'
    paginate_by = 10

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.accept = True
        return super().form_valid(form)

    def get_queryset(self):
        # Получаем обычный запрос
        user = self.request.user
        return Feedback.objects.filter(advert__author__user=user)


