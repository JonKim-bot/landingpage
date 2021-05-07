from django.urls import path

from . import views

urlpatterns = [
    # path('home/', views.home, name='api-home'),
    path('about/', views.about_list),
    path('get_home/', views.get_home, name='get_home'),
    path('home/', views.home_list),
    path('insert_form/', views.insert_form),

    path('home/<int:pk>/', views.home_detail),
    
    # path('about/<int:pk>/', views.about_detail),
    # path('', views.home, name='blog-home'),
    # path('api_test', views.api_test, name='api_test'),

    # path('about', views.about, name='blog-about'),
]