from django.db import models

STATE = (
  (0, 'new'),
  (1, 'used'),
)

class Dealer(models.Model):
  name = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  
def __str__(self):
  return self.name

  
class Car(models.Model):
  brand = models.CharField(max_length=30)
  model = models.CharField(max_length=30)
  price = models.FloatField()
  matriculation = models.DateField()
  km = models.IntegerField()
  state = models.IntegerField(STATE)
  color = models.CharField(max_length=30)
  traction = models.CharField(max_length=30)
  dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name="dealer_cars")
  
  def __str__(self):
      return f"{self.brand} {self.model}"
  