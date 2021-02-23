from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png',blank=True)
    

    def __str__(self):
        return self.title

    def snippet(self):
        if len(self.body) > 50:
            return self.body[:50] + '...'
        else:
            return self.body