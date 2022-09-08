""" Videos Views"""
# Django
from datetime import timedelta

# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
# Models


def index(request):
    return render(request=request,template_name="videos/index.html")