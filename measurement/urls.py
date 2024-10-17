from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('sensors/', views.SensorList.as_view()),
    path('measurements/create/', views.MeasurementCreate.as_view()),
    path('sensors/create/', views.SensorCreate.as_view()),
    path('sensors/<int:pk>/', views.SensorDetail.as_view()),
  
]