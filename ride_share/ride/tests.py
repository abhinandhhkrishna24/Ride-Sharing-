from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Ride, Rider, User

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.rider = Rider.objects.create(user=self.user)
    
    def test_ride_creation(self):
        ride = Ride.objects.create(rider=self.rider, pickup_location="Location A", dropoff_location="Location B")
        self.assertEqual(ride.status, "requested")
     

class APITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(self.user)

def test_create_ride(self):
    url = reverse('ride_create')
    data = {'pickup_location': 'Location A', 'dropoff_location': 'Location B'}
    response = self.client.post(url, data, format='json')
    print(response.content)  
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
 
