from django.db import models


class Breed(models.Model):
    size_choices = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    name = models.CharField(max_length=100, verbose_name='Порода')
    size = models.CharField(max_length=10, choices=size_choices)
    friendliness = models.IntegerField(validators=[models.Min(1), models.Max(5)])
    trainability = models.IntegerField(validators=[models.Min(1), models.Max(5)])
    shedding_amount = models.IntegerField(validators=[models.Min(1), models.Max(5)])
    exercise_needs = models.IntegerField(validators=[models.Min(1), models.Max(5)])
    
    def __str__(self) -> str:
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    age = models.IntegerField()
    breed = models.ForeignKey(to=Breed, on_delete=models.SET_DEFAULT, default=None)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=50)

