from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.welcome, name="WELCOME"),
    path('home', views.home, name="HOME"),
    path('aboutus', views.aboutus, name="ABOUT"),
    path('login', views.LOGIN, name="LOGIN"),
    path('signup', views.signup, name="SIGNUP"),
    path('prediction/', views.prediction, name="PREDICTION"),
    path('prediction/result/', views.result, name="result"),
]
