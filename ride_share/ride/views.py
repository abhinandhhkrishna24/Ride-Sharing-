from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserCreateSerializer, UserLoginSerializer,RideSerializer
from .models import Ride, Driver
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


# Create your views here.


class UserRegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=201)
        return Response(serializer.errors, status=400)
    

class UserLoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=200)
        return Response({'error': 'Invalid credentials'}, status=401)


class CreateRideView(generics.CreateAPIView):
    serializer_class=RideSerializer
    permission_classes=[IsAuthenticated]


class RideDetailView(generics.RetrieveAPIView):
    queryset =Ride.objects.all()
    serializer_class= RideSerializer
    permission_classes=[IsAuthenticated]

class RideListsView(generics.ListAPIView):
    queryset=Ride.objects.all()
    serializer_class =RideSerializer
    permission_classes=[IsAuthenticated]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

class RideUpdateStatusView(generics.UpdateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        status_value = request.data.get('status')  
        if status_value in ['started', 'completed', 'cancelled']:
            instance.status = status_value
            instance.save()
            return Response({'message': 'Ride status updated successfully'}, status=status.HTTP_200_OK) 
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)



class AvailableRidesView(generics.ListAPIView):
    queryset = Ride.objects.filter(status='requested')
    serializer_class = RideSerializer

    def get(self, request, *args, **kwargs):
        available_rides = self.get_queryset()

        if available_rides.exists():
            ride = available_rides.first() 
            available_drivers = Driver.objects.filter(availability='available')

            if available_drivers.exists():
                driver = available_drivers.first() 
                ride.driver = driver 
                ride.status = 'accepted' 
                ride.save()
                return Response({'message': 'Ride request matched successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'No available drivers'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'No available rides'}, status=status.HTTP_404_NOT_FOUND)
        


class AcceptRideView(generics.UpdateAPIView):
    queryset = Ride.objects.filter(status='requested')
    serializer_class = RideSerializer

    def put(self, request, *args, **kwargs):
        ride = self.get_object()
        driver = request.user.driver

        if driver and driver.availability == 'available':
            if ride.status == 'accepted' and ride.driver is None:
                ride.driver = driver
                ride.status = 'started'
                ride.save()
                return Response({'message': 'Ride request accepted successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Ride request is not available for acceptance'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Driver is not available'}, status=status.HTTP_400_BAD_REQUEST)