# Generated by Django 3.1.7 on 2021-04-26 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_two', models.TextField()),
                ('list_content', models.TextField()),
                ('detail_word', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('image2', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('notable_client', models.TextField()),
                ('consulatation_word', models.TextField()),
                ('limited_discount', models.TextField()),
                ('button_text', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]