from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10, default='random')

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"