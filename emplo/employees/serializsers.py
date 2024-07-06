from rest_framework import serializers
from .models import Position, Employee

class PositionSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()
    class Meta:
        model = Position
        fields = ['id', 'name', 'parent', 'children', 'parent_name']
    
    def get_parent_name(self, obj):
        return obj.parent.name if obj.parent else None

class EmployeeSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'parent', 'position_name']
    
    def get_position_name(self, obj):
        return obj.position.name
