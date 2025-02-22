from rest_framework.serializers import ModelSerializer, IntegerField
from app.models import Dog, Breed


class DogsSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class BreedsSerializer(ModelSerializer):

    dog_count = IntegerField(source='dogs.count', read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"