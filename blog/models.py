from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title
