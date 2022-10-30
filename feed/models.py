from django.db import models
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=20)
    tweet = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)