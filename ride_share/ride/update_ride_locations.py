from django.core.management.base import BaseCommand
from .models import Ride
import random

class Command(BaseCommand):
    help = 'Update ride locations periodically'

    def handle(self, *args, **options):
        rides = Ride.objects.filter(status='started')[:100] 

        for ride in rides:
            try:
                step_size = 0.001 
                ride.live_latitude += random.uniform(-step_size, step_size)
                ride.live_longitude += random.uniform(-step_size, step_size)
                ride.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error updating ride location: {e}"))
