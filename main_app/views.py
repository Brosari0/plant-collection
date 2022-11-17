from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Plant, Continent
from .forms import WateringForm

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
    id_list = plant.continents.all().values_list('id')
    continents_plant_isnt_in = Continent.objects.exclude(id__in=id_list)
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', { 
        'plant': plant, 'watering_form': watering_form, 
        'continents': continents_plant_isnt_in 
        })
        
class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'family', 'description']

class PlantUpdate(UpdateView):
    model = Plant
    fields = '__all__'

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

class ContinentList(ListView):
    model = Continent

class ContinentDetail(DetailView):
    model = Continent

class ContinentCreate(CreateView):
    model = Continent
    fields = ['name']

class ContinentUpdate(UpdateView):
    model = Continent
    fields = ['name']

class ContinentDelete(DeleteView):
    model = Continent
    success_url = '/continents'

def assoc_continent(request, plant_id, continent_id):
    Plant.objects.get(id=plant_id).continents.add(continent_id)
    return redirect('detail', plant_id=plant_id)

def disassoc_continent(request, plant_id, continent_id):
    Plant.objects.get(id=plant_id).continents.remove(continent_id)
    return redirect('detail', plant_id=plant_id)