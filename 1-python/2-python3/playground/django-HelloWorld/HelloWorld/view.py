# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    print("arrived here")
    context = {}
    context['hello'] = 'Hello s World!'
    return HttpResponse('hello.html')