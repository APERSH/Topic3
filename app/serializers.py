from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField
from app.models import Dog, Breed
from django.db.models import Avg

# Сериализатор для модели Dog
class DogsSerializer(ModelSerializer):
    # Поля для дополнительной информации: количество собак той же породы и средний возраст
    same_breed_count = SerializerMethodField()
    average_age = SerializerMethodField()

    class Meta:
        model = Dog
        fields = "__all__"

    # Метод для получения получения собак той же породы
    def get_same_breed_count(self, obj : Dog):
        """
        Возвращает количество собак той же породы
        """
        if isinstance(self.instance, Dog):
            return obj.breed.dogs.count()
        return None
    
    # Метод для получения получения собак той же породы
    def get_average_age(self, obj : Dog):
        """
        Возвращает средний возраст собак той же породы.
        Используется агрегация для вычисления среднего возраста.
        """
        breed_avg_age = Dog.objects.filter(breed = obj.breed).aggregate(Avg('age'))['age__avg']
        return breed_avg_age
        
# Сериализатор для модели Breed
class BreedsSerializer(ModelSerializer):
    # Поле для отображения количества собак этой породы
    dog_count = IntegerField(source='dogs.count', read_only=True)
    
    class Meta:
        model = Breed
        fields = "__all__"