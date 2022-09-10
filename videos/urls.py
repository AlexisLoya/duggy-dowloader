""" Videos Urls"""
# Django
from django.urls import path
# Views
from videos import views

urlpatterns = [
    path(
        route='',
        view=views.index,
        name='index'
    ),
    path(
        route='download',
        view=views.download,
        name='download'
    )
]
