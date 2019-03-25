from django.urls import path
from .views import *

urlpatterns = [
    path('', CarrierList.as_view()),
    path('create/', CarrierCreate.as_view()),
    path('update/<int:pk>/', CarrierRetrieveUpdate.as_view()),
]