from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from task import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'task')  # Cambiado de 'task' a 'tasks'

urlpatterns = [
    path('', include(router.urls)),  # Eliminado "api/v1"
    path('docs/', include_docs_urls(title="Task API"))
]