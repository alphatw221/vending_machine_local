from django.urls import path
from .views import *



urlpatterns = [
    
    
    #api
    path('synchronize/',Synchronize.as_view()),
    path('set_price/',SetPrice.as_view()),
    path('set_stock/',SetStock.as_view()),
    path('rest/',Rest.as_view()),
    path('start/',Start.as_view()),
 
]