from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plant_index, name='plant_index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail')
]