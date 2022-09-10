""" Videos Views"""
# Django
from datetime import timedelta

# Django
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
# Models
from videos.models import Video
# Pytuve
from pytube import YouTube


# Models


def index(request):
    return render(request=request, template_name="videos/index.html")


def download(request):
    if request.method == 'POST':
        try:
            video: YouTube = YouTube(request.POST.get('url'))
            resolutions = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            for resolution in resolutions:
                print(type(resolution))
                print(resolution)

            return render(
                request,
                "videos/index.html",
                {'resolutions': resolutions}
            )
        except:
            print(request.POST.get('url'))

    return render(
        request,
        "videos/index.html"
    )


def get_resolutions(video: YouTube):
    """ Get all resolution for resolution """
    resolution_sort = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    return resolution_sort
