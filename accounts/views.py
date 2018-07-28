# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.
# import logging
# logger = logging.getLogger(__name__)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list') # name of the url in the articles app
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            #log user in
            user = form.get_user() # rtrieve the user
            login(request, user)  # log the user in
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list') # name of the url in the articles app

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        # logger.error("here!")
        return redirect('articles:list')
    # else:
    #     return HttpResponse("DIDN'T WORK")