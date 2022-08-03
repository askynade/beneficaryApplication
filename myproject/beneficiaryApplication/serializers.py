from rest_framework import serializers
from beneficiaryApplication.models import Application,District,Taluka


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class TalukaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taluka
        fields = "__all__"
        
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
        
        