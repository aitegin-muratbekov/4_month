"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main1 import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', views.index_view),
    path('about_us/', views.about_us_view),
    path('time/', views.date_now),
    path('films/', views.film_list_view),
    path('film/<int:id>/', views.film_detail_view),
    path('directors/', views.directors_view),
    path('director/<int:id>/films/', views.director_detail_view)
]
