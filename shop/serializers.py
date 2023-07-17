from rest_framework import serializers
from .models import Car, Dealer


class DealerSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Dealer
    fields = "__all__"
    
    
class CarSerializer(serializers.ModelSerializer):
  dealer = serializers.PrimaryKeyRelatedField(queryset=Dealer.objects.all())
  
  class Meta:
    model = Car
    fields = "__all__"
    
  # def create(self, validated_data):
  #   dealer_id = validated_data
  #   print(dealer_id)
  #   print("ostia!!!")
  #   car = Car.objects.create(**validated_data)
  #   return car
  