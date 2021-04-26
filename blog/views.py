from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User
import json
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.core import serializers

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1', 
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def home(request):
    userfirst = User.objects.all()
    userfilter = User.objects.filter(username="emmwee").first()
    userid = userfilter.id
    user  = User.objects.get(id=1 )
    # Post1 = Post(title="Test",content = "first test",author = user)
    # Post1.save()
    all_post = Post.objects.all()
    # user_post = user.post_set()
    user_post = user.post_set.all()
    # user_post_create = user.post_set.create(title= "user create",content = "user create post")
    # user_post_create.save()
    # get user with that post
    context = {
        'posts': user_post,
        'title' : userfilter,
    }
    return render(request, 'blog/home.html', context)

def api_test(request):
    userfirst = User.objects.all()
    userfilter = User.objects.filter(username="emmwee").first()
    userid = userfilter.id
    user  = User.objects.get(id=1 )
    # Post1 = Post(title="Test",content = "first test",author = user)
    # Post1.save()
    all_post = Post.objects.all()
    # user_post = user.post_set()
    user_post = user.post_set.all()
    Postquery = Post.objects.raw('SELECT * FROM blog_post LIMIT 2')
    data = serializers.serialize("json", Postquery)
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
