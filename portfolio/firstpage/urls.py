from .views import index , orderform, success, videos, ethiocal
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('order/', orderform, name='order'),
    path('success/', success , name='success'),
    path('video/', videos , name= 'videos'),
    path('ethiocal/', ethiocal , name= 'ethiocal' ),
]