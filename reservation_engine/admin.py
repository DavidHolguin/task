from django.contrib import admin
from .models import Property, RoomType, Room, Guest, Reservation, ReservationChannel, ChannelReservation, PropertyImage, RoomTypeImage, RoomTypeVideo

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'is_logo', 'caption')
    list_filter = ('is_logo',)
    search_fields = ('property__name', 'caption')
    autocomplete_fields = ['property']

@admin.register(RoomTypeImage)
class RoomTypeImageAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'property_name', 'caption')
    search_fields = ('room_type__name', 'room_type__property__name', 'caption')
    autocomplete_fields = ['room_type']

    def property_name(self, obj):
        return obj.room_type.property.name
    property_name.short_description = 'Property'

@admin.register(RoomTypeVideo)
class RoomTypeVideoAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'property_name', 'caption')
    search_fields = ('room_type__name', 'room_type__property__name', 'caption')
    autocomplete_fields = ['room_type']

    def property_name(self, obj):
        return obj.room_type.property.name
    property_name.short_description = 'Property'

# Registro de los otros modelos ya configurados
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'property', 'capacity', 'base_price')
    list_filter = ('property',)
    search_fields = ('name', 'property__name')
    autocomplete_fields = ['property']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'property', 'room_type', 'is_available')
    list_filter = ('property', 'room_type', 'is_available')
    search_fields = ('room_number', 'property__name')
    autocomplete_fields = ['property', 'room_type']

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'user__email', 'phone_number')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'guest', 'room', 'check_in_date', 'check_out_date', 'status', 'total_amount')
    list_filter = ('property', 'status', 'check_in_date', 'check_out_date')
    search_fields = ('guest__user__username', 'guest__user__email', 'property__name', 'room__room_number')
    date_hierarchy = 'check_in_date'
    autocomplete_fields = ['property', 'guest', 'room']

@admin.register(ReservationChannel)
class ReservationChannelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ChannelReservation)
class ChannelReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'channel', 'external_reservation_id')
    list_filter = ('channel',)
    search_fields = ('external_reservation_id', 'reservation__guest__user__username', 'channel__name')
    autocomplete_fields = ['reservation', 'channel']
