from rest_framework.serializers import ModelSerializer
from .models import Room
from .models import Amenity
from users.serialziers import TinyUserSerialzer
from categories.serializers import CategorySereializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerialzer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySereializer(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )
