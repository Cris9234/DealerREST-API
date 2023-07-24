from django.urls import path
from .views import (
    dealer_cars, 
    delete_car,
    get_car, 
    get_cars, 
    post_car, 
    update_car,
    get_dealer,
    post_dealer,
    update_dealer,
    delete_dealer,
    CarMaxKm,
  )
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('cars/get_car/', get_car, name="get_car"),
  path('cars/get_cars/', get_cars, name="get_cars"),
  path('cars/post_car/', post_car, name="post_car"),
  path('cars/delete_car/', delete_car, name="car_delete"),
  path('cars/update_car/', update_car, name="update_car"),
  path('cars/filter/', CarMaxKm.as_view(), name="max_km"),
  path('dealer/get_dealer/', get_dealer, name="get_dealer"),
  path('dealer/post_dealer/', post_dealer, name="post_dealer"),
  path('dealer/update_dealer/', update_dealer, name="update_dealer"),
  path('dealer/delete_dealer/', delete_dealer, name="delete_dealer"),
  path('dealer_cars/<int:pk>/', dealer_cars, name="dealer_cars"),
]

urlpatterns = format_suffix_patterns(urlpatterns)