
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Measurement
from .serializers import MeasurementSerializer, SensorSerializer,SensorDetailSerializer


class MeasurementList(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()


class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorList(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorSerializer


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorDetailSerializer



class SensorCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'measurements': reverse('measurement-list', request=request),
        'sensors': reverse('sensor-list', request=request),
    })

@api_view(['POST'])
def create_measurement(request, format=None):
    serializer = MeasurementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_measurement(request, pk, format=None):
    measurement = get_object_or_404(Measurement, pk=pk)
    serializer = MeasurementSerializer(measurement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)