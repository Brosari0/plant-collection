# Generated by Django 4.1.3 on 2022-11-16 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['-date']},
        ),
    ]
