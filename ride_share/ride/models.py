from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

class User(AbstractUser):
    pass



class Driver(models.Model):
    AVAILABILITY = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('offline', 'Offline')
    ]

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    availability = models.CharField(max_length=10, choices=AVAILABILITY, default='available')
    current_location = models.CharField(max_length=200,null=True, blank=True)
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Rider(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='Ride_rider', blank=False, null=False)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='Ride_driver', null=True, blank=True)
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    live_location = models.CharField(max_length=200,null=True, blank=True)
    live_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    live_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    def __str__(self):
        return f"Ride #{self.id} - {self.rider.user.username}"
