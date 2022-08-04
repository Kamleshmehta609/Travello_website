from django.urls import path
from . import views

urlpatterns=[
 path('Mumbai',views.Mumbai, name='Mumbai'),
 path('Hyderabad',views.Hyderabad, name='Hyderabad'),
 path('Pune',views.Pune, name='Pune')
]