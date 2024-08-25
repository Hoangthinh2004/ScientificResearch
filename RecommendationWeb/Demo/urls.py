from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('university/', views.listUniversity, name="list-university"),
    path('university/<str:pk>', views.showOneUniversity, name="show-one-university"),
    path('major/', views.listMajor, name="list-major"),
    path('major/<str:pk>', views.showOneMajor, name="show-one-major"),
    path('unimajor/<str:uid>/<str:mid>', views.showOneMajor, name="show-one-major"),
    

]