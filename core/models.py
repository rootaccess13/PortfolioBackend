from unicodedata import name
from django.db import models

# Create your models here.


class githubRepos(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    html_url = models.URLField()

    def __str__(self):
        return self.name
