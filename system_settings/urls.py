from django.urls import path

from system_settings import views

app_name = 'system_settings'

urlpatterns = [
    path('location/add/', views.CreateLocation.as_view(), name='location_add'),
    path('unit/add/', views.CreateUnit.as_view(), name='unit_add'),
    path('airport/add/', views.CreateAirport.as_view(), name='airport_add')
]
