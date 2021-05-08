from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User
import json
from home.models import Home
from home.models import Landingform

from about.models import About

from home.serializers import HomeSerializer
from rest_framework.response import Response
# serializer = HomeSerializer()
from rest_framework.decorators import api_view, renderer_classes

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.serializers import LandingformSerializer

from home.serializers import HomeSerializer
from about.serializers import AboutSerializer

from django.core import serializers
from landingpage.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


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
@api_view(['GET','POST'])
@csrf_exempt
def insert_form(request):
    """
    List all code home, or create a new home.
    """

    # if request.
    if  request.method == 'POST' or request.method == "GET":
  
        serializer = LandingformSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            subject = 'Welcome to DataFlair'
            message = 'Hope you are enjoying your Django Tutorials'
            recepient = str(serializer.data.email)
            send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET','POST'])
@csrf_exempt
def about_list(request):
    """
    List all code home, or create a new home.
    """
    try:
        about = About.objects.all()

    except About.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    # if request.
    if request.method == 'GET' or request.method == 'POST':
        # home = Home.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)

        # return JsonResponse(serializer.data, safe=False)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = HomeSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
@api_view(['GET','POST'])
@csrf_exempt
def home_list(request):
    """
    List all code home, or create a new home.
    """
    try:
        home = Home.objects.all()

    except Home.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    # if request.
    if request.method == 'GET' or request.method == 'POST':
        # home = Home.objects.all()
        serializer = HomeSerializer(home, many=True)
        return Response(serializer.data)

        # return JsonResponse(serializer.data, safe=False)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = HomeSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
@api_view(['GET','POST'])

@csrf_exempt
def home_detail(request, pk):
    """
    Retrieve, update or delete a code home.
    """
    try:
        home = Home.objects.get(pk=pk)
    except Home.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' or request.method == 'POST' :
        serializer = HomeSerializer(home, many=False)
        return Response(serializer.data)

        # return JsonResponse(serializer.data)

    elif request.method == 'PUT' :
        data = JSONParser().parse(request)
        serializer = HomeSerializer(home, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        home.delete()
        return HttpResponse(status=204)
def get_home(request):
    # return HttpResponse(repr(serializer))

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
    # return HttpResponse(data)

# def about(request):
#     # if request.method == 'POST':

#     about = About.objects.all()
#     # # user_post = user.post_set()
#     # user_post = user.post_set.all()
#     # Postquery = Post.objects.raw('SELECT * FROM blog_post LIMIT 2')
#     data = serializers.serialize("json", about)
#         # data = json.loads(data)

#         # data= type(data)


#         # cars = ["Ford", "Volvo", "BMW"]
#         # cars = cars[0]
#     return HttpResponse(data)

#     # return render(request, 'blog/about.html')

#     # return HttpResponse("about")
