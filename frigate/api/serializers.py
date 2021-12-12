from users.models import Parking_place
from rest_framework import serializers


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Parking_place
