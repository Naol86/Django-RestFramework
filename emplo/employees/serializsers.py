from rest_framework import serializers
from .models import Position, Employee

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'parent', 'children']

class EmployeeSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'position_name']
    
    def get_position_name(self, obj):
        return obj.position.name
