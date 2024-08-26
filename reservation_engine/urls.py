from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, RoomTypeViewSet, RoomViewSet, GuestViewSet, ReservationViewSet, ReservationChannelViewSet, ChannelReservationViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'roomtypes', RoomTypeViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'guests', GuestViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'channels', ReservationChannelViewSet)
router.register(r'channel-reservations', ChannelReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]