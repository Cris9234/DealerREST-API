from .models import Car, Dealer
from .serializers import CarSerializer, DealerSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Car
# FBV

@api_view(['GET'])
def get_cars(request):
  cars = Car.objects.all()
  serializer = CarSerializer(cars, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_car(request):
  car_id = request.GET.get('car_id')
  try:
    car = Car.objects.get(id=car_id)
    serializer = CarSerializer(car)
    return Response(serializer.data)
  except Car.DoesNotExist:
    return Response({"Error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

 
@api_view(['POST'])
def post_car(request):
  serializer = CarSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"Success": "Car has been created"} ,status=status.HTTP_204_NO_CONTENT)
  return Response({"Error": "Car has not been saved"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_car(request):
  car_id = request.GET.get('car_id')
  try:
    car = Car.objects.get(id=car_id)
  except Car.DoesNotExist:
    return Response({"Error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
  serializer = CarSerializer(car, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response({"Error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request):
  car_id = request.GET.get('car_id')
  try:
    car = Car.objects.get(id=car_id)
  except Car.DoesNotExist:
    return Response({"Error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
  car.delete()
  return Response({"Success": "Car has been deleted"} ,status=status.HTTP_204_NO_CONTENT)

# CBV

class AllCars(generics.ListAPIView):
  queryset = Car.objects.all()
  serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Car.objects.all()
  serializer_class = CarSerializer

class CarMaxKm(generics.ListAPIView):
  serializer_class = CarSerializer
  
  def get_queryset(self):
    max_km = self.request.query_params.get("max_km")
    return Car.objects.filter(km__lt=max_km)
  

# Dealer
# FBV

@api_view(['GET'])
def get_dealer(request):
  dealer_id = request.GET.get('dealer_id')
  try:
    dealer = Dealer.objects.get(id=dealer_id)
    serializer = DealerSerializer(dealer)
    return Response(serializer.data)
  except Dealer.DoesNotExist:
    return Response({"Error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_dealer(request):
  serializer = DealerSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response({"Success": "Dealer has been created"} ,status=status.HTTP_204_NO_CONTENT)
  return Response({"Error": "Dealer has not been saved"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_dealer(request):
  dealer_id = request.GET.get('dealer_id')
  try:
    dealer = Dealer.objects.get(id=dealer_id)
  except Dealer.DoesNotExist:
    return Response({"Error": "Dealer not found"}, status=status.HTTP_404_NOT_FOUND)
  serializer = DealerSerializer(dealer, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response({"Error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_dealer(request):
  dealer_id = request.GET.get('dealer_id')
  try:
    dealer = Dealer.objects.get(id=dealer_id)
  except Dealer.DoesNotExist:
    return Response({"Error": "Dealer not found"}, status=status.HTTP_404_NOT_FOUND)
  dealer.delete()
  return Response({"Success": "Dealer has been deleted"} ,status=status.HTTP_204_NO_CONTENT)
    
  
@api_view(['GET'])
def dealer_cars(request, pk):
  if request.method == 'GET':
    dealer = Dealer.objects.get(pk=pk)
    dealer_cars = dealer.dealer_cars.all()
    serializer = CarSerializer(dealer_cars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
