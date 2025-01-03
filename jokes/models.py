from django.db import models
from django.urls import reverse 
from common.utils.text import unique_slug

class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
    max_length=50, unique=True, null=True, editable=False
)
    def get_absolute_url(self):
        return reverse('jokes:detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
