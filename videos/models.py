""" Videos Models """
# Django
from django.db import models
# Models
from Duggy.utils.models import DuggyModel


# Create your models here.
class Video(DuggyModel):
    """Model to save the data for each video downloaded"""
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    length = models.PositiveBigIntegerField()

