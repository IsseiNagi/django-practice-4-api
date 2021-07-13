from django.contrib import admin
from django.urls import path
from .views import TopView, WeatherAPIView

urlpatterns = [
    path('top/', TopView.as_view(), name='top'),
    # API
    path('api/<int:pk>/', WeatherAPIView.as_view(), name='api')
]
