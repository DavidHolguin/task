from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('task.urls')),
    path('api/reservation/', include('reservation_engine.urls')),    
]
