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
    
class Landingform(models.Model):
    landing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'landingform'
