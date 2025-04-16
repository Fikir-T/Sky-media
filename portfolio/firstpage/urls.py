from .views import index , orderform, success
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('order/', orderform, name='order'),
    path('success/', success , name='success')
]