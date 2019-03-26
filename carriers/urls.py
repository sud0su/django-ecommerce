from django.urls import path
from .views import *

urlpatterns = [
    path('list/', CarrierList.as_view(), name="carriers-all"),
    path('create/', CarrierCreate.as_view()),
    path('update/<int:pk>/', CarrierRetrieveUpdate.as_view()),
]