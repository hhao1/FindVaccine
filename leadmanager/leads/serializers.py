from rest_framework import serializers
from leads.models import Lead
from leads.models import Vaccine
from leads.models import Makers


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = "__all__"


class MakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Makers
        fields = "__all__"
