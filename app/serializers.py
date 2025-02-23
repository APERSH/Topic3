from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField
from app.models import Dog, Breed
from django.db.models import Avg


class DogsSerializer(ModelSerializer):
    same_breed_count = SerializerMethodField()
    average_age = SerializerMethodField()

    class Meta:
        model = Dog
        fields = "__all__"

    def get_same_breed_count(self, obj):
        if isinstance(self.instance, Dog):
            return obj.breed.dogs.count()
        return None
    
    def get_average_age(self, obj):
        breed_avg_age = Dog.objects.filter(breed = obj.breed).aggregate(Avg('age'))['age__avg']
        return breed_avg_age
        

class BreedsSerializer(ModelSerializer):

    dog_count = IntegerField(source='dogs.count', read_only=True)
    
    class Meta:
        model = Breed
        fields = "__all__"