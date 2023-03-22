from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.pk)])

    def __str__(self):
        return self.title