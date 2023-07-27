from rest_framework import serializers
from .models import Category


class CategorySereializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        # exclude = ("created_at",)
