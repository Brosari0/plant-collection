from django.shortcuts import render
from .models import Plant

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plant_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants
    })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', { 'plant': plant })