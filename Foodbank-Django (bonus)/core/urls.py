from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('add-food/', views.add_food, name='add_food'),
    path('distribute/', views.distribute, name='distribute'),
    path('report/', views.report, name='report'),

    # Family management
    path('families/manage/', views.manage_families, name='manage_families'),
    path(
        'families/delete/<int:family_id>/',
        views.delete_family,
        name='delete_family'
    ),
]