from django.urls import path

from . import views

urlpatterns = [
    # path('home/', views.home, name='api-home'),
    path('about/', views.about, name='api-about'),
    path('get_home/', views.get_home, name='get_home'),
    path('home/', views.snippet_list),
    path('home/<int:pk>/', views.snippet_detail),
    # path('', views.home, name='blog-home'),
    # path('api_test', views.api_test, name='api_test'),

    # path('about', views.about, name='blog-about'),
]