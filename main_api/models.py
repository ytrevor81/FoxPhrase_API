from django.db import models

class Deck(models.Model):
    user = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100, null=True)
    deck_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    words = models.TextField()
    published = models.DateField("Uploaded on")
    likes = models.IntegerField(null=True)
    downloads = models.IntegerField(null=True)
    #comments = models.TextField(null=True)

    def __str__(self):
        return self.user + "'s " + self.deck_name
