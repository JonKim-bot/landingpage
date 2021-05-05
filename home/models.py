from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse


class Home(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,default='')
    button_text = models.CharField(max_length=255,default='')
    # subtitle = models.CharField()
    about_title = models.TextField(default='')
    about_description = models.TextField(default='')

    service_title = models.TextField(default='')
    # content = models.TextField()
    # content_two = models.TextField()
    list_content = models.TextField(default='')
    detail_word = models.TextField(default='')
    imageone = models.ImageField(default='default.jpg', upload_to='profile_pics')
    imagetwo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    imagethree = models.ImageField(default='default.jpg', upload_to='profile_pics')
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
