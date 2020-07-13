from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Room

# By using ModelSerializer, you don't need to serialize every elements in model
class RoomSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "beds",
            "instant_book",
            "user",
        )

# serialize means to convert types
# class RoomSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=140)
#     price = serializers.IntegerField()
#     bedrooms = serializers.IntegerField()
#     instant_book = serializers.BooleanField()

class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()