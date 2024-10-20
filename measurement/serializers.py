from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensor']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
