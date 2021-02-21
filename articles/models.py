from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    #thumbnail =
    #author =
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) > 50:
            return self.body[:50] + '...'
        else:
            return self.body