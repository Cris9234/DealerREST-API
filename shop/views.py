from .models import Car
from .serializers import CarSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def car_list(request, format=None):
  if request.method == 'GET':
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk, format=None):
  try:
    car = Car.objects.get(pk=pk)
  except Car.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = CarSerializer(car)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class AllCars(generics.ListAPIView):
  queryset = Car.objects.all()
  serializer_class = CarSerializer
  
class Car10000Km(generics.ListAPIView):
  queryset = Car.objects.filter(km__lt = 100000)
  serializer_class = CarSerializer