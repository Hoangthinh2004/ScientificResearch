from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('university/', views.listUniversity, name="list-university"),
    path('university/<str:pk>', views.showOneUniversity, name="show-one-university"),
    path('major/', views.listMajor, name="list-major"),
    path('major/<str:pk>', views.showOneMajor, name="show-one-major"),
    path('university/<str:pk>', views.showOneUniversity, name="show-one-university"),
    path('filter/', views.filter, name="filter"),
    path('university/filter/', views.filter, name="filter-university"),
    path('university/filter/<str:pk>/', views.filterInOneUniversity, name="filter-one-university"),
    path('major/filter/', views.filter, name="filter-major"),
    path('major/filter/<str:pk>/', views.filterInOneMajor, name="filter-one-major"),
    

]