from django.db import models
from django.urls import reverse
from datetime import date


WATERED = (
    ('T', 'Watered'),
    ('F', 'Not Watered')
)

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

    def watered_for_today(self):
        return self.watering_set.filter(date=date.today()).count() >= (len(WATERED) - 1)

class Watering(models.Model):
    date = models.DateField('Watering Date')
    watered = models.CharField(
        max_length=1,
        choices=WATERED,
        default=WATERED[0][0]
    )

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_watered_display()} on {self.date}"

    class Meta: 
        ordering = ['-date']