from leads.models import Lead
from leads.models import Vaccine
from leads.models import Makers
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from .serializers import VaccineSerializer
from .serializers import MakersSerializer


# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

# Vaccine Viewset


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VaccineSerializer


class MakersViewSet(viewsets.ModelViewSet):
    queryset = Makers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MakersSerializer
