from django.urls import path
from .views import Home, CreateFlight, ListFlights

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('createFlight/', CreateFlight.as_view(), name='createFlight'),
    path('listFlights/', ListFlights.as_view(), name='listFlights'),
]