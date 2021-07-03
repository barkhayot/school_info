from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    ranking = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    website = models.URLField()

    def __str__(self):
        return self.name