from django.contrib import admin
from app.models import Dog, Breed

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

