from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Carrier
from .serializers import CarriersSerializer

# Note viewset
# CRUD via API
class CarrierViewSet(viewsets.ModelViewSet):
    # check permission
    permission_classes = (IsAuthenticated,)
    queryset = Carrier.objects.all()
    serializer_class =CarriersSerializer 
    Lookup_field = 'id'