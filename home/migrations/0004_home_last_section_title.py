# Generated by Django 3.1.7 on 2021-05-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210506_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='last_section_title',
            field=models.TextField(default=''),
        ),
    ]
