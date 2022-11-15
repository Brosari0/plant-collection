from django.shortcuts import render

# Create your views here.
plants = [
    {'name': 'East Asian Cherry', 'family': 'Rosaceae', 'description': 'Sweetly fragrant, the cherry blossoms stand upright at the side of the branches. Opening from pink buds, the large saucer-shaped blooms, almost 2 in. across (4.5 cm), count up to 6-15 petals. They fade to almost white as they mature and display a purplish pink heart just before shedding.'},
    {'name': 'Swiss Cheese Plant', 'family': 'Araceae', 'description': 'Swiss Cheese Plant is named so because of its huge leaves with holes in them that resembles Swiss cheese. Leaf shape changes as the leaves mature from entire to having holes to eventually having perforations often extending to and breaking through the outer edges of the leaves and result in a pinnatifid leaf shape.'},
    {'name': 'Foxtail Agave', 'family': 'Asparagaceae', 'description': 'The Foxtail Agave is an evergreen succulent. It has stiff blue-green leaves with spiny edges growing in a dense rosette. During the last year of its life, it produces a single flower stalk up to 4.5m long with pale greenish yellow flowers.'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plant_index(request):
    return render(request, 'plants/index.html', {
        'plants':plants
    })