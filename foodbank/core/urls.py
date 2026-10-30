from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('add/', views.add_food, name='add_food'),
    path('distribute/', views.distribute, name='distribute'),
    path('report/', views.report, name='report'),
]
