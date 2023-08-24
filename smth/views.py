from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Article


class LView(LoginRequiredMixin, View):
    raise_exception = True
    login_url = '/login/'


class ArticleCreate(CreateView, LoginRequiredMixin):
    permission_required = ('basis.add_article',)
    model = Article
    template_name = 'article_create.html'


class ArticleEdit(UpdateView, LoginRequiredMixin):
    permission_required = ('basis.update_article',)
    model = Article
    template_name = 'article_edit.html'


class ArticleDelete(DeleteView, LoginRequiredMixin):
    permission_required = ('basis.delete_article',)
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('/news/')


