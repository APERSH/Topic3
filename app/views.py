from rest_framework.viewsets import ModelViewSet
from app.models import Dog, Breed
from app.serializers import DogsSerializer, BreedsSerializer

# ViewSet для модели Dog
class DogViewSet(ModelViewSet):
    """
    ViewSet для работы с собаками.
    Предоставляет все стандартные действия для модели Dog:
    - Получение списка всех собак
    - Создание новой собаки
    - Получение информации о конкретной собаке
    - Обновление информации о собаке
    - Удаление собаки
    """
    queryset = Dog.objects.all()
    serializer_class = DogsSerializer


# ViewSet для модели Breed
class BreedViewSet(ModelViewSet):
    """
    ViewSet для работы с породами собак.
    Предоставляет все стандартные действия для модели Breed:
    - Получение списка всех пород
    - Создание новой породы
    - Получение информации о конкретной породе
    - Обновление информации о породе
    - Удаление породы
    """
    queryset = Breed.objects.all()
    serializer_class = BreedsSerializer
    