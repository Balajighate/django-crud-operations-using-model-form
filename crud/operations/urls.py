from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.Add, name='add'),
    path('delete/<str:id>', views.Delete, name='delete'),
    path('edit', views.Edit, name='edit'),
    path('update/<str:id>', views.update, name ='update'),
    path('mysite', views.mysite, name='mysite'),

]
