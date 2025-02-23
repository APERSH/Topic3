import json
from rest_framework.test import APITestCase
from app.models import Dog, Breed
from django.urls import reverse
from app.serializers import DogsSerializer
from rest_framework import status


class DogApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.breed = Breed.objects.create(
           name = "Labrador", 
           size = "Large", 
           friendliness = 5,
           trainability = 4, 
           shedding_amount = 3,
           exercise_needs = 4
        )
        self.dog1 =  Dog.objects.create(
            name = "Alex",
            age = 5,
            breed = self.breed,
            gender = "Male",
            color = "Brown",
            favorite_food = "Beef",
            favorite_toy = "Ball"           
        )
        self.dog2 = Dog.objects.create(
            name = "Max",
            age = 3,
            breed = self.breed,
            gender = "Male",
            color = "Gray",
            favorite_food = "Chicken",
            favorite_toy = "Ball"           
        )

    def test_get(self):
        url = reverse("dogs-list")
        response = self.client.get(url)
        serializer_data = DogsSerializer([self.dog1, self.dog2], many = True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(serializer_data[0]['average_age'], 4)

    def test_create(self):
        self.assertEqual(2, Dog.objects.all().count())
        url = reverse("dogs-list")
        data = {
            "name" : "Ben",
            "age" : 2,
            "breed" : self.breed.id,
            "gender" : "Male",
            "color" : "Brown",
            "favorite_food" : "Beef",
            "favorite_toy" : "Ball" 
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data = json_data, content_type = 'application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Dog.objects.all().count())

    def test_get_detail(self):
        url = reverse("dogs-detail", args=(self.dog1.id,))
        response = self.client.get(url)
        serializer_data = DogsSerializer(self.dog1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(serializer_data['same_breed_count'], 2)

    def test_update(self):
        url = reverse("dogs-detail", args=(self.dog1.id,))
        data = {
            "name" : self.dog1.name,
            "age" : 20,
            "breed" : self.dog1.breed.id,
            "gender" : self.dog1.gender,
            "color" : self.dog1.color,
            "favorite_food" : self.dog1.favorite_food,
            "favorite_toy" : self.dog1.favorite_toy 
        }
        json_data = json.dumps(data)
        response = self.client.put(url, data = json_data, content_type = 'application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.dog1.refresh_from_db()
        self.assertEqual(20, self.dog1.age)

    def test_delete(self):
        self.assertEqual(2, Dog.objects.all().count())
        url = reverse("dogs-detail", args=(self.dog1.id,))
        data = {
            "name" : self.dog1.name,
            "age" : self.dog1.age,
            "breed" : self.dog1.breed.id,
            "gender" : self.dog1.gender,
            "color" : self.dog1.color,
            "favorite_food" : self.dog1.favorite_food,
            "favorite_toy" : self.dog1.favorite_toy
        }
        json_data = json.dumps(data)
        response = self.client.delete(url, data = json_data, content_type = 'application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Dog.objects.all().count())

        
        