# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import WriterForm


def index(request):
    return render(request, 'verby/index.html')
def writer_signup(request):
    form = WriterForm()

    if request.method == 'POST':
        form = WriterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return publications(request)

        else:

            print form.errors

    return render(request, 'verby/writer_signup.html', {'form': form})


def publications(request):
    return render(request, 'publications.html')
