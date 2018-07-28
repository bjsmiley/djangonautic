# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

def article_list(request):
    
    articles = Article.objects.all().order_by('date')

    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context )

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)

    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context)

@login_required(login_url='/account/login/')
def article_create(request):
    return render(request, 'articles/article_create.html')