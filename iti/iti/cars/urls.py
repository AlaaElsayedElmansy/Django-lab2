from django.urls import path
from cars.views import carsIndex, CarDetails, CreateCarView , EditCarView ,DeleteCarView 
urlpatterns = [    
    path('index', carsIndex ),
    path('<int:pk>',CarDetails.as_view(), name='cars.show'),
    path('create', CreateCarView.as_view() )  , 
    path('edit/<int:pk>',EditCarView.as_view(), name='cars.edit'),
    path('delete/<int:pk>',DeleteCarView.as_view(), name='cars.delete'),
]

  
