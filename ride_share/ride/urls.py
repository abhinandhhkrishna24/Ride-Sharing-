from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    CreateRideView,
    RideDetailView,
    RideListsView,
    RideUpdateStatusView,
    AvailableRidesView,
    CreateRideView, 
    AcceptRideView   
)

urlpatterns = [
    path('user/register/', UserRegisterView.as_view(), name='user_register'),
    path('user/login/', UserLoginView.as_view(), name='user_login'),

    path('ride/create/', CreateRideView.as_view(), name='ride_create'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride_detail'),
    path('ride/lists/', RideListsView.as_view(), name='rides_list'),
    path('ride/<int:pk>/update/', RideUpdateStatusView.as_view(), name='ride_status_update'),

    path('ride/available/', AvailableRidesView.as_view(), name='available_rides'),
    path('ride/accept/<int:pk>/', AcceptRideView.as_view(), name='accept_ride'),
]

