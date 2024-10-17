
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer, SensorListSerializer




class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer
        if self.request.method in ['PUT', 'PATCH']:
            return SensorSerializer


class SensorCreate(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'measurements': reverse('measurement-list', request=request),
        'sensors': reverse('sensor-list', request=request),
    })
