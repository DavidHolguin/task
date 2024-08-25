from rest_framework import serializers
from .models import Task  # Asegúrate de que esta importación sea correcta

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Cambia 'task' por Task (sin comillas)
        fields = '__all__'