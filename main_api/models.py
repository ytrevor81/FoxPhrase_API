from django.db import models

class Decks(models.Model):
    user = models.CharField(max_length=100)
    deck_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    words = models.TextField()
    published = models.DateField("Uploaded on")
    likes = models.IntegerField()
    comments = models.TextField()
