from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# from .models import Question
from .models import About
class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    # summernote_fields = '__all__'
    summernote_fields = ('content_two',)


admin.site.register(About,AboutAdmin)
# admin.site.register(Choice)