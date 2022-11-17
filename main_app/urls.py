from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plant_index, name='plant_index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plant_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),

    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),

    path('plants/<int:plant_id>/assoc_continent/<int:continent_id>/', views.assoc_continent, name='assoc_continent'),
    path('plants/<int:plant_id>/disassoc_continent/<int:continent_id>/', views.disassoc_continent, name='disassoc_continent'),

    path('continents/', views.ContinentList.as_view(), name='continents_index'),
    path('continents/<int:pk>/', views.ContinentDetail.as_view(), name='continents_detail'),
    path('continents/create/', views.ContinentCreate.as_view(), name='continents_create'),
    path('continents/<int:pk>/update/', views.ContinentUpdate.as_view(), name='continents_update'),
    path('continents/<int:pk>/delete/', views.ContinentDelete.as_view(), name='continents_delete'),
]