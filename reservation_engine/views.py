from rest_framework import viewsets
from .models import Property, RoomType, Room, Guest, Reservation, ReservationChannel, ChannelReservation
from .serializers import PropertySerializer, RoomTypeSerializer, RoomSerializer, GuestSerializer, ReservationSerializer, ReservationChannelSerializer, ChannelReservationSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationChannelViewSet(viewsets.ModelViewSet):
    queryset = ReservationChannel.objects.all()
    serializer_class = ReservationChannelSerializer

class ChannelReservationViewSet(viewsets.ModelViewSet):
    queryset = ChannelReservation.objects.all()
    serializer_class = ChannelReservationSerializer