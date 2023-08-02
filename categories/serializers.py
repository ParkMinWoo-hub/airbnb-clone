from rest_framework import serializers
from .models import Category


class CategorySereializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )
        # exclude = ("created_at",)
