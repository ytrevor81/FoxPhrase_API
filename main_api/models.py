from django.db import models

class Deck(models.Model):
    user = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100, null=True)
    deck_name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    words = models.TextField()
    published = models.DateField("Uploaded on")
    downloads = models.IntegerField(null=True)

    def __str__(self):
        return self.user + "'s " + self.deck_name
