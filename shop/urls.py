from django.urls import path
from .views import AllCars, Car10000Km, car_list, car_detail, index
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', index, name="index"),
  path('cars/', car_list, name="car_list"),
  path("cars/<int:pk>/", car_detail, name="car_detail"),
  path('all_cars/', AllCars.as_view(), name="all_cars"),
  path('lessthen/', Car10000Km.as_view(), name='lt10000'),
]

urlpatterns = format_suffix_patterns(urlpatterns)