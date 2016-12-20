"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label='app'

class Play(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    class Meta:
        app_label='app'

class Line(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=20)
    text = models.CharField(max_length=400)
    speech_no = models.IntegerField(null=True)
    speaker = models.ForeignKey(Speaker)
    play = models.ForeignKey(Play)
    
    class Meta:
        app_label='app'
