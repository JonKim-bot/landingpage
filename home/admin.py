from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# from .models import Question
from .models import Home
class HomeAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Home,HomeAdmin)
# admin.site.register(Choice)