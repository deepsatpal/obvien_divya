from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index2'),
    path('twitter-callback', views.twitter_callback, name='index1'),
]