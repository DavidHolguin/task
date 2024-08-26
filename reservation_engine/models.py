from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    # Añade más campos según sea necesario
    def __str__(self):
        return self.name

class RoomType(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=100)  # e.g., 'Single', 'Double', 'Family'
    capacity = models.IntegerField()
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.name} - {self.property.name}"

class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.room_number} - {self.property.name}"

class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.user.email})"
    # Añade más campos según sea necesario

class Reservation(models.Model):
    RESERVATION_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reservations')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_adults = models.IntegerField()
    number_of_children = models.IntegerField()
    currency = models.CharField(max_length=3)  # e.g., 'USD', 'EUR'
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Reservation {self.id} - {self.guest} - {self.property.name}"

class ReservationChannel(models.Model):
    name = models.CharField(max_length=100)  # e.g., 'Direct', 'Booking.com', 'Expedia'
    def __str__(self):
        return self.name

class ChannelReservation(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='channel_reservation')
    channel = models.ForeignKey(ReservationChannel, on_delete=models.CASCADE)
    external_reservation_id = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.channel.name} - {self.external_reservation_id}"
    
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    is_logo = models.BooleanField(default=False)  # Si es el logo de la propiedad
    caption = models.CharField(max_length=255, blank=True)  # Descripción opcional
    def __str__(self):
        return f"{self.property.name} - {'Logo' if self.is_logo else 'Image'}"

class RoomTypeImage(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_type_images/')
    caption = models.CharField(max_length=255, blank=True)  # Descripción opcional
    def __str__(self):
        return f"{self.room_type.name} - {self.room_type.property.name}"

class RoomTypeVideo(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='room_type_videos/')
    caption = models.CharField(max_length=255, blank=True)  # Descripción opcional
    def __str__(self):
        return f"{self.room_type.name} - {self.room_type.property.name}"
