from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = "__all__"
        # fields = ['id', 'title', 'content', 'content_two', 'list_content', 'detail_word','image','date_posted']