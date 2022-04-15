from rest_framework import serializers
from .models import Profile


class ProfileSerializers(serializers.Serializer):
    Name = serializers.CharField(max_length=100)
    city = serializers.IntegerField()

    def create(self,validate_data):
        return Profile.objects.create(**validate_data)


    
