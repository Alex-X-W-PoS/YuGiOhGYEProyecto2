# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def torneos(request):
    return render(request,'landing/torneos.html',{})
