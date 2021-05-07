from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,default="")
    # subtitle = models.CharField()
    content = models.TextField()
    content_two = models.TextField()
    list_content = models.TextField()
    detail_word = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image2 = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    notable_client = models.TextField()

    consulatation_word = models.TextField()
    limited_discount = models.TextField()
    button_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    