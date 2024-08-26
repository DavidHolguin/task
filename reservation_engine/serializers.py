from rest_framework import serializers
from .models import Property, RoomType, Room, Guest, Reservation, ReservationChannel, ChannelReservation

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationChannel
        fields = '__all__'

class ChannelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelReservation
        fields = '__all__'
        