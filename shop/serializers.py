from rest_framework import serializers
from .models import Car, Dealer


class DealerSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Dealer
    fields = "__all__"
    
    
class CarSerializer(serializers.ModelSerializer):
  dealer = DealerSerializer(read_only=True)
  
  class Meta:
    model = Car
    fields = "__all__"
    
  def create(self, validated_data):
    dealer_data = self.initial_data.get('dealer')
    dealer_id = dealer_data.get('id')
    if not dealer_id:
      raise serializers.ValidationError("Dealer ID is required.")
    try:
      dealer = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
      raise serializers.ValidationError("Dealer with the provided ID does not exist")
    car = Car.objects.create(dealer=dealer, **validated_data)
    return car
  
  def update(self, instance, validated_data):
    dealer_data = self.initial_data.get('dealer')
    dealer_id = dealer_data.get('id')
    
    if not dealer_id:
      raise serializers.ValidationError("Dealer ID is required.")
    
    for attr, value in validated_data.items():
      setattr(instance, attr, value)
    instance.save()
    return instance
      
      

  