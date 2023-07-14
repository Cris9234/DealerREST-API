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
  