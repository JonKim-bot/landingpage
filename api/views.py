from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User
import json
from home.models import Home
from about.models import About

from django.core import serializers


# def home(request):
#     userfirst = User.objects.all()
#     userfilter = User.objects.filter(username="emmwee").first()
#     userid = userfilter.id
#     user  = User.objects.get(id=1 )
#     # Post1 = Post(title="Test",content = "first test",author = user)
#     # Post1.save()
#     all_post = Post.objects.all()
#     # user_post = user.post_set()
#     user_post = user.post_set.all()
#     # user_post_create = user.post_set.create(title= "user create",content = "user create post")
#     # user_post_create.save()
#     # get user with that post
#     context = {
#         'posts': user_post,
#         'title' : userfilter,
#     }
#     return render(request, 'blog/home.html', context)

def get_home(request):
    # userfirst = User.objects.all()
    # userfilter = User.objects.filter(username="emmwee").first()
    # userid = userfilter.id
    # user  = User.objects.get(id=1 )
    # Post1 = Post(title="Test",content = "first test",author = user)
    # Post1.save()
    if request.method == 'POST':

        home = Home.objects.all()
        # # user_post = user.post_set()
        # user_post = user.post_set.all()
        # Postquery = Post.objects.raw('SELECT * FROM blog_post LIMIT 2')
        data = serializers.serialize("json", home)
        # data = json.loads(data)

        # data= type(data)


        # cars = ["Ford", "Volvo", "BMW"]
        # cars = cars[0]
        return HttpResponse(data)

    # final = []
    # for row in data:
    #     return HttpResponse(data)

    #     final.append(row.field)
    # data = serializers.serialize("json", final)

    # # user_post_create = user.post_set.create(title= "user create",content = "user create post")
    # # user_post_create.save()
    # # get user with that post
    # context = {
    #     'posts': user_post,
    #     'title' : userfilter,
    # }
    # return render(request, 'blog/home.html', context)
    return HttpResponse(data)

def about(request):
    return render(request, 'blog/about.html')

    # return HttpResponse("about")
