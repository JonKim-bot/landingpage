from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse


class Home(models.Model):
    title = models.CharField(max_length=255)
    # subtitle = models.CharField()
    content = models.TextField()
    content_two = models.TextField()
    list_content = models.TextField()
    detail_word = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    