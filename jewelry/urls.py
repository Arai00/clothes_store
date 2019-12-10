from django.urls import path
from . import views

urlpatterns=[
    path('', views.jewelry, name='jewelry'),
    path('<int:pk>', views.details, name='details'),
    path('payfor/<int:pk>', views.paymentJ, name='payJ'),

]