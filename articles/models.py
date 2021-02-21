from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    #thumbnail =
    #author =
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()