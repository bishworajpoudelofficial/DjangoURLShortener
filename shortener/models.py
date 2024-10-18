from django.db import models

# Create your models here.
class MyURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"