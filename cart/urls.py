from django.urls import path
from . import views

urlpatterns=[
    path('cart/clothes/<int:pk>', views.cartClothes, name='cartCloth'),
    path('cart/jewelry/<int:pk>', views.cartJew, name='cartJew'),
    path('', views.cartshow, name='cartshow'),
    path('delete', views.delete, name='delete'),
    path('payment', views.pay, name='payment'),
    path('delete1/<int:pk>', views.deletepro, name='deletebyone')
]