from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import FeedbackFilter
from django.shortcuts import redirect
from django.core.mail import send_mail
# from django.conf.settings import DEFAULT_FROM_EMAIL
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
        advert.author = user
        return super().form_valid(form)

class AdvertUpdate(UserPassesTestMixin, UpdateView):
    permission_required = ('Build_Board.change_post',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Advert
    # и новый шаблон, в котором используется форма.
    template_name = 'advert_edit.html'

    def test_func(self):
        item = self.get_object()
        return item.author == self.request.user

    # def form_valid(self, form):
    #     news = form.save(commit=False)
    #     news.choice = 'NS'
    #     return super().form_valid(form)


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_edit.html'

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        return super().form_valid(form)


def feedback_confirm(request, pk):
    feed = Feedback.objects.get(pk=pk)
    feed.accept = True
    feed.save()
    send_mail(
        subject='Принятие отклика',
        message=f'Автор объявления {feed.advert.author.username} принял ваш отклик',
        from_email=None,
        recipient_list=[feed.user.email],
    )
    return redirect(request.META['HTTP_REFERER']) # Перенаправляет на туже самую страницу с которой был запрос

class ProfillUser(ListView):
    # queryset = Feedback.objects.filter(advert__author=user)
    template_name = 'profil_user.html'
    context_object_name = 'feedbacks_user'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        queryset = Feedback.objects.filter(advert__author=user)
        self.filterset = FeedbackFilter(self.request.GET, queryset)
        return self.filterset.qs

    # Переопределяем функцию получения списка товаров
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

#
#     template_name = 'feedback.html'
#     context_object_name = 'feedbacks'
#     paginate_by = 10
#
#     def form_valid(self, form):
#         feedback = form.save(commit=False)
#         feedback.accept = True
#         return super().form_valid(form)
#
#     def get_queryset(self):
#         # Получаем обычный запрос
#         user = self.request.user
#         return Feedback.objects.filter(advert__author=user)


