"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from festivals.views import * 
from jwt_auth.views import * 
from attending.views import AttendingPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('festivals/', FestivalList.as_view()),
    path('festivals/<int:pk>/', FestivalUpdateDestroy.as_view()),
    path('festival/<int:pk>/', FestivalById.as_view()),
    path('festivalsearch/', getFestivalByName.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('hotels/', HotelList.as_view()),
    path('hotels/<int:pk>/', HotelUpdateDestroy.as_view()),
    path('hotel/<int:pk>/', HotelById.as_view()),
    path('user/<int:pk>/', UserById.as_view()),
    path('post/', AttendingPost.as_view()),
    path('message/', SendMessage.as_view()),
    path('all-messages/', getAllMessages.as_view()),
    path('my-messages/', getMyMessages.as_view()),
    path('messages/', getFriendsMessages.as_view()),
    #path('friend-request/<int:pk>', friendRequest.as_view())
    
]
