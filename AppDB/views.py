from django.shortcuts import render
from .forms import *


def render_tamplate(tpl, dt, request):
    """
    :param tpl: html template
    :param dt: dictionary to send
    :param request: HTTP request
    :return: HTML with base
    """
    dct = {}
    dct.update(dt)
    return render(request, tpl, dct)


def home(request):
    activity = OcActivity.objects.all()
    form = DataTableForm()
    return render_tamplate('index.html', {'act': activity, 'form': form}, request)
