from rest_framework import fields, serializers
from .models import Task

class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'